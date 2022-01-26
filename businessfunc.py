from lib2to3.pgen2 import token
from urllib import request
from customizetool import *
from getvatinvoicedtl import *
from getgenericocr import *
from getbaidutoken import *
from transimage2excel import *

def VAT2TXT(parameter:str):
    tokenstr = getBaiduToken(conf_path=parameter)
    inpath = getSourceFilePath(parafile=parameter)
    outputpath = getOutputPath(parafile=parameter)
    fileset = overtraversalFile(dirpath=inpath)
    rtnDataset = []
    for file in fileset:
        resultpath = ''.join([inpath,file])
        print(resultpath)
        data = getVATInvoice(
        token=tokenstr,
        imgpath=resultpath,
        dtlflag=False
        )
        if data[0] == 0:
            rtnDataset.append(','.join(data[1]))
        else:
            raise Exception('error message = ',data)
    print(rtnDataset)
    writeData2File(fpath=outputpath,fname='invoice_list.txt',indata=changeResult2Data(indata=rtnDataset))
    return rtnDataset

def OCR2TXT():
    pass

def IMG2EXCEL(parameter:str):
    tokenstr = getBaiduToken(conf_path=parameter)
    inpath = getSourceFilePath(parafile=parameter)
    outputpath = getOutputPath(parafile=parameter)
    fileset = overtraversalFile(dirpath=inpath)
    rtnDataset = []
    for file in fileset:
        resultpath = ''.join([inpath,file])
        data = postIMG(
            token=tokenstr,
            imgpath=resultpath
            )
        print(data,'type of :',type(data))
        if data[0] == 0:
            rtnDataset.append(data[1].get('result')[0].get('request_id'))
        else:
            raise Exception('error message = ',data)
    # getdata = getTransData(token=tokenstr,requestid=rtnDataset)
    print('post img request rtn data is:',rtnDataset)
    # print('get excel data request rtn data is:',getdata)
    return rtnDataset

def GETOCREXCEL(parameter:str,ridset:list):
    tokenstr = getBaiduToken(conf_path=parameter)
    getdata = getTransData(token=tokenstr,requestid=ridset)
    print('get excel data request rtn data is:',getdata)