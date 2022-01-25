# 上传图片至ocr地址
# 异步获取上传后转出文件
import requests
import os.path
import base64
import time
from customizetool import getFileSize,resizeImage

def postIMG(token:str,imgpath:str):
    apiUrl = 'https://aip.baidubce.com/rest/2.0/solution/v1/form_ocr/request'
    imageType = os.path.splitext(imgpath)[-1].upper()
    imgfile = open(file=imgpath,mode='rb')
    fileSize = getFileSize(fpath=imgpath)
    print(fileSize)
    if fileSize > 1024:
        # if image file too large to trans,resize it
        # 20210608 resize function has some probleam???
        rs = resizeImage(ipath=imgpath,ratio=0.75)
        b64Img = base64.b64encode(rs[1])
    else:
        b64Img = base64.b64encode(imgfile.read())

    apiUrlheaders = {
        'content-type':'application/x-www-form-urlencoded'
    }
    if imageType in ['.JPG','.JPEG','.PNG','.BMP']:
        apiUrlPara = {
            'access_token':token,
            'image':b64Img,
            'is_sync':'false',
            'request_type':'excel'
        }
    else:
        raise Exception('input image filetype not in [jpg,jpeg,png,bmp], please check filetype')

    try:
        r = requests.post(url=apiUrl,data=apiUrlPara,headers=apiUrlheaders)
        rtnData = r.json()
        print(rtnData)
        if rtnData.get('error_code') is not None:
            rstList = [rtnData.get('error_code'),rtnData.get('error_msg')]
            raise Exception(rtnData.get('error_code'),rtnData.get('error_msg'))
        else:
            resultData = rtnData.get('result')
            # make a special list for baiwang invoice scaner page
            # change data style
            newDateStyle = ''.join(list(filter(str.isdigit,resultData.get('InvoiceDate'))))
            
    except Exception as err:
        print(err)

    return 0,rtnData

def getTransData(token:str,requestid:str):
    pass