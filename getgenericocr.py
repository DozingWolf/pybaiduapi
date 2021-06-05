import requests
import os.path
import base64
from enum import Enum,unique
from customizetool import getFileSize,resizeImage,pdfToImg

@unique
class languageType(Enum):
    CHN_ENG='CHN_ENG'
    ENG='ENG'
    JAP='JAP'
    KOR='KOR'
    FRE='FRE'
    SPA='SPA'
    POR='POR'
    GER='GER'
    ITA='ITA'
    RUS='RUS'

def getGenericOCR(token,imgpath,langtype:languageType=languageType.CHN_ENG,direction:bool=False,paragraph:bool=False):
    apiUrl = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
    apiUrlheaders = {
        'content-type':'application/x-www-form-urlencoded'
    }
    apiUrlPara = {
            'access_token':token
        }
    imageType = os.path.splitext(imgpath)[-1].upper()
    imgFile = open(file=imgpath,mode='rb')
    fileSize = getFileSize(fpath=imgpath)
    print('file size = ',fileSize)
    apiUrlPara.update({
        'language_type':langtype.value,
        'detect_direction':str(direction),
        'paragraph':str(paragraph)
    })
    if imageType in ['.JPG','.JPEG','.PNG','.BMP']:
        if fileSize > 1024:
            # if image file too large to trans,resize it
            rs = resizeImage(ipath=imgpath,ratio=0.75)
            b64Img = base64.b64encode(rs)
        else:
            b64Img = base64.b64encode(imgFile.read())
        apiUrlPara.update({
            'image':b64Img
        })
        apiRtnData = postDataToOCRApi(url=apiUrl,para=apiUrlPara,head=apiUrlheaders)
        print(apiRtnData)
    elif imageType == '.PDF':
        apiRtnDataList = []
        # raise Exception('developer was too busy to support type pdf now!:(')
        for tRoot,tDirs,tFiles in os.walk(pdfToImg(ppath=imgpath)):
            print(''.join([tRoot,tFiles]))
            tImgFile = open(file=''.join([tRoot,tFiles]),mode='rb')
            b64Img = base64.b64encode(tImgFile)
            apiUrlPara.update({
                'image':b64Img
            })
            apiRtnDataTemp = postDataToOCRApi(url=apiUrl,para=apiUrlPara,head=apiUrlheaders)
            apiRtnDataList.append()
            tImgFile.close()
        print(apiRtnDataList)
    else:
        raise Exception('input image filetype not in [pdf,jpg,jpeg,png,bmp], please check filetype')
    
def postDataToOCRApi(url:str,para:dict,head:dict):
    try:
        r = requests.post(url=url,data=para,headers=head)
        rtnData = r.json()
        return rtnData
    except Exception as err:
        print(err)
