from businessfunc import VAT2TXT,IMG2EXCEL,GETOCREXCEL

if __name__ == '__main__':
    para = './conf/para.conf'
    VAT2TXT(parameter=para)
    # rid = IMG2EXCEL(parameter=para)
    # GETOCREXCEL(parameter=para,ridset=['23744705_3047447'])