import os.path
from PIL import Image

def getFileSize(fpath,unit='KB'):
    
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
    
def resizeImage(ipath,ratio=0.75,saveflag='N'):
    if ratio > 1:
        raise Exception('customize resizeImage function only can make a pic small')
    i = Image.open(ipath)
    fileName = ''.join([os.path.splitext(ipath)[0],'_resize',os.path.splitext(ipath)[-1]])
    fileType = os.path.splitext(ipath)[-1][1:]
    iw,ih = i.size
    nIw = int(iw*ratio)
    nIh = int(ih*ratio)
    i = i.resize((nIw,nIh),Image.ANTIALIAS)
    if saveflag == 'N':
        return 0,i
    elif saveflag == 'Y':
        i.save(fileName,fileType)
        return 0,i
    else:
        raise Exception('Error saveflag has been input')