# 获取百度接口使用的token和aksk
from configparser import ConfigParser
import requests
import json
import sqlite3
import os.path
import time

def getBaiduToken(conf_path):
    paraLoader = ConfigParser()
    paraLoader.read(conf_path)
    ai_ak = paraLoader.get('baidu_ai','ak')
    ai_sk = paraLoader.get('baidu_ai','sk')
    map_ak = paraLoader.get('baidu_map','ak')
    baseDir = os.path.dirname(os.path.abspath(__file__))
    absPath = os.path.join(baseDir,'storage\Token.db')
    print('create db')
    dbHandle = sqlite3.connect(absPath)
    dbCursor = dbHandle.cursor()
    countSql = 'select count(1) from sqlite_master where name = "Token"' 
    dbCursor.execute(countSql)
    dbReturn = dbCursor.fetchall()
    print('dbReturn[0][0]:',dbReturn[0][0])
    if dbReturn[0][0] == 0:
        print('create table')
        dbCreateTable = 'CREATE TABLE Token (id integer PRIMARY KEY autoincrement,tokentype varchar(20),accesstoken varchar(500),accesskey varchar(500))'
        dbCursor.execute(dbCreateTable)
        urlFlag,urlData = requestsAIToken(ai_ak,ai_sk)
        print('urlflag : ',urlFlag)
        print('urlData : ',urlData)
        rtnToken = urlData[0]
        insertSql = 'INSERT INTO Token(tokentype,accesstoken,accesskey) VALUES(?,?,?)'
        insertPara = ('BaiduAI',urlData[0],urlData[1])
        try:
            dbCursor.execute(insertSql,insertPara)
            dbHandle.commit()
            dbReturn = dbCursor.fetchall()
            print(dbReturn)
        except Exception as err:
            print(err)
    else:
        dbSql = 'select count(1) from Token where tokentype = ?'
        dbSqlParaTokenType = 'BaiduAI'
        dbCursor.execute(dbSql,(dbSqlParaTokenType,))
        dbReturn = dbCursor.fetchall()
        if dbReturn[0][0] == 1:
            print('DB has data')
            selectSql = 'select accesstoken,accesskey from Token where tokentype = ?'
            dbCursor.execute(selectSql,(dbSqlParaTokenType,))
            dbReturn = dbCursor.fetchall()
            print('sql result = ',dbReturn)
            rtnToken = dbReturn[0][0]
        else:
            print('DB hasn`t data')
            urlFlag,urlData = requestsAIToken(ai_ak,ai_sk)
            if urlFlag == 0:
                insertSql = 'INSERT INTO Token(tokentype,accesstoken,accesskey) VALUES(?,?,?)'
                insertPara = ('BaiduAI',urlData[0],urlData[1])
                dbCursor.execute(insertSql,insertPara)
                dbHandle.commit()
                rtnToken = urlData[0]
                if dbCursor.rowcount == 1:
                    pass
                else:
                    raise Exception('update date error')
            else:
                raise Exception(''.join(urlData))
    dbCursor.close()
    dbHandle.commit()
    return rtnToken

    
def requestsAIToken(akkey,skkey):
    baiduAITokenUrl = 'https://aip.baidubce.com/oauth/2.0/token'
    baiduAITokenPara = {
        'grant_type':'client_credentials',
        'client_id':akkey,
        'client_secret':skkey
    }
    r = requests.get(url=baiduAITokenUrl,params=baiduAITokenPara)
    formatData = json.loads(r.text)
    if formatData.get('access_token') is not None:
        return 0,[formatData.get('access_token'),formatData.get('session_key'),formatData.get('session_secret')]
    elif formatData.get('error') is not None:
        return -1,['None Data']
        # raise Exception(formatData.get('error'))

def delExpiredToken(ttype):
    baseDir = os.path.dirname(os.path.abspath(__file__))
    absPath = os.path.join(baseDir,'storage\Token.db')
    dbHandle = sqlite3.connect(absPath)
    dbCursor = dbHandle.cursor()
    deleteSql = 'delete from Token where tokentype = ?'
    deleteSqlPara = (ttype,)
    try:
        dbCursor.execute(deleteSql,deleteSqlPara)
    except Exception as err:
        print(err)
        dbCursor.close()
        return -1,['err']
    dbHandle.commit()
    dbCursor.close()
    return 0,['Delete Success']

getBaiduToken(conf_path = './conf/para.conf')
#delExpiredToken(ttype='Baidu')