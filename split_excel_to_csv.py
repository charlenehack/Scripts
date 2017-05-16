# -*- coding: utf-8 -*-

import xlrd
import csv
import os


def read_excel(file_name):
    excel = xlrd.open_workbook(file_name, encoding_override='utf8')
    for excel_sheet in excel.sheets():
        for i in range(excel_sheet.nrows):
            yield excel_sheet.row_values(i)
            
    
class Csv(object):
    def __init__(self, name):
        self.f = open(name + u'.csv', 'wb')
        self.write = csv.writer(self.f, quoting=csv.QUOTE_MINIMAL)
        
    def writerow(self,lst):
        self.write.writerow(lst)
        
    def save(self):
        self.f.close()
                                              

def encode(s):
    if isinstance(s, unicode):
        try:
            s.encode('gbk')
        except Exception:
            print s
        return s.encode('gbk')
    elif isinstance(s, str):
        return s
    elif isinstance(s,float) and s > 10000000:
        return str(int(s))
    else:
        return s
    

def find_xls():
    files = [
        name for name in os.listdir(os.getcwd()) if name.endswith(('.xlsx','.xls'))
    ]
    return files


def main():
    sites = dict()
    i = 1
    for row_data in read_excel(find_xls()[0]):
        if i == 1:
            heads = row_data
            i = 0
            continue
        site_name = row_data[1]
        if site_name not in sites:
            site_obj = Csv(site_name)
            sites[site_name] = site_obj
            #data = map(encode, row_data)
            site_obj.writerow(map(encode, heads))
            site_obj.writerow(map(encode, row_data))
        else:
            #data = map(encode, row_data)
            sites[site_name].writerow(map(encode, row_data))
    for site in sites.values():
        site.save()
if __name__ == '__main__':
    main()
    
