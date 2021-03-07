# 获取增值税发票票面信息
import requests
import os.path
import base64
import time
from customizetool import getFileSize,resizeImage

def getVATInvoice(token,imgpath):
    apiUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice'
    imageType = os.path.splitext(imgpath)[-1].upper()
    imgfile = open(file=imgpath,mode='rb')
    fileSize = getFileSize(fpath=imgpath)
    print(fileSize)
    if fileSize > 1024:
        # if image file too large to trans,resize it
        rs = resizeImage(ipath=imgpath,ratio=0.75)
    b64Img = base64.b64encode(imgfile.read())
    apiUrlheaders = {
        'content-type':'application/x-www-form-urlencoded'
    }
    if imageType == '.PDF':
        apiUrlPara = {
            'access_token':token,
            'pdf_file':b64Img,
            'type':'normal'
        }
    elif imageType in ['.JPG','.JPEG','.PNG','.BMP']:
        apiUrlPara = {
            'access_token':token,
            'image':b64Img,
            'type':'normal'
        }
    else:
        raise Exception('input image filetype not in [pdf,jpg,jpeg,png,bmp], please check filetype')
    try:
        r = requests.post(url=apiUrl,data=apiUrlPara,headers=apiUrlheaders)
        rtnData = r.json()
        print(rtnData)
        resultData = rtnData.get('words_result')
        rstList = [
            resultData.get('InvoiceNum'),resultData.get('InvoiceCode'),resultData.get('InvoiceType'),
            resultData.get('InvoiceDate'),resultData.get('SellerName'),resultData.get('TotalAmount'),
            resultData.get('TotalTax'),resultData.get('Remarks')
        ]
        return 0,rstList
    except Exception as err:
        print(err)
    if rtnData.get('error_code') is not None:
        raise Exception(rtnData.get('error_msg'))
