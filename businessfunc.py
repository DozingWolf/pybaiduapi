from customizetool import *
from getvatinvoicedtl import *
from getgenericocr import *
from getbaidutoken import *

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