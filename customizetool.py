from os import error,listdir
import os.path
from tempfile import TemporaryFile,TemporaryDirectory
import fitz
from fitz import open,Matrix,preRotate
from PIL import Image
from configparser import ConfigParser
import json

def getFileSize(fpath:str,unit:str='KB'):
    
    if unit == 'KB':
        # return filesize by KB
        size = os.path.getsize(fpath)/float(1024)
        return round(size,2)
    elif unit == 'MB':
        # return filesize by MB
        size = os.path.getsize(fpath)/float(1024)/float(1024)
        return round(size,2)
    else:
        return -1
    
def resizeImage(ipath:str,ratio:float=0.75,saveflag:bool=False):
    if ratio > 1:
        raise Exception('customize resizeImage function only can make a pic small')
    i = Image.open(ipath)
    fileName = ''.join([os.path.splitext(ipath)[0],'_resize',os.path.splitext(ipath)[-1]])
    fileType = os.path.splitext(ipath)[-1][1:]
    iw,ih = i.size
    nIw = int(iw*ratio)
    nIh = int(ih*ratio)
    i = i.resize((nIw,nIh),Image.ANTIALIAS)
    if saveflag == False:
        return 0,i
    elif saveflag == True:
        i.save(fileName,fileType)
        return 0,i
    else:
        raise Exception('Error saveflag has been input')

def pdfToImg(ppath:str,zoomrate:float=1.3333,saveflag:bool=False,savepath:str=''):
    pdfFile = fitz.open(ppath)
    transImgList = []
    print(pdfFile.pageCount)
    with TemporaryDirectory() as tempDirPath:
        print(tempDirPath)
        for i in range(pdfFile.pageCount):
            aPDFPage = pdfFile[i]
            enlarge = fitz.Matrix(zoomrate,zoomrate).preRotate(int(0))
            aPixPage = aPDFPage.getPixmap(matrix=enlarge, alpha=False)
            if saveflag == False:
                tempImgFile = ''.join([tempDirPath,str(i),'.png'])
                aPixPage.writePNG(tempImgFile)
                # transImgList.append(aPixPage)
                return tempDirPath
            else:
                saveFile = ''.join([savepath,'\\',str(i),'.png'])
                print(saveFile)
                aPixPage.writePNG(saveFile)
                return -1

def getSourceFilePath(parafile:str):
    try:
        paraLoader = ConfigParser()
        paraLoader.read(parafile)
        filepath = paraLoader.get('source','path')
        return filepath
    except Exception as err:
        print('getSourceFilePath error:')
        print(err) 

def overtraversalFile(dirpath:str):
    fileset = listdir(dirpath)
    print(fileset)
    return fileset

def getOutputPath(parafile:str):
    try:
        paraLoader = ConfigParser()
        paraLoader.read(parafile)
        filepath = paraLoader.get('output','path')
        return filepath
    except Exception as err:
        print('getOutputPath error:')
        print(err)

def changeResult2Data(indata):
    if type(indata) == dict:
        rtnData = json.dumps(indata)
    elif type(indata) == tuple:
        rtnData = '\n'.join(indata)
    elif type(indata) == list:
        rtnData = '\n'.join(indata)
    else:
        datatype = type(indata)
        raise Exception('Error indata with changeResult2Data ,indata type =',datatype,' ,indata =',indata)
    return rtnData

def writeData2File(fpath,fname,indata):
    filePath = ''.join([fpath,fname])
    with open(filePath,'w') as f:
        f.write(indata)