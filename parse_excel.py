#!/bin/env python
#coding:utf8

import xlwt
import xlrd
import os

#定义读出EXCEL数据，EXCEL所有的行数据转换成一个大的字典，value是行值{1:[vlaue,vale2...]}
def read_excel(file_name):
    try:
        excel_obj = xlrd.open_workbook(file_name)
        excel_sheet = excel_obj.sheets()[0]
        lst_dict = {} 
        for row in range(excel_sheet.nrows):
            lst_dict[row] = excel_sheet.row_values(row)
        return lst_dict
    except Exception,e:
        print e


#定义提取函数，提取出lst_dict只要的列值，返回一个字典。key为lst[1],values为lst[3]
def cre_dict(lst_dict):
    if not lst_dict:
        raise "lst_dict is None"
    dic = {}
    for lst in lst_dict.values():
        if not dic.get(lst[1],None):
            dic[lst[1]] = round(float(lst[3]),3)
        else:
            dic[lst[1]] += round(float(lst[3]),3)
    return dic


#定义汇总函数，将result_dic去除重复key并汇总value
def count_dic(args):
    sum_dic = {}
    for arg in args:
       for key in arg.keys():
           if not sum_dic.get(key):
               sum_dic[key] = arg[key]
           else:
               sum_dic[key] += arg[key]
    return sum_dic 

    

#定义相减的函数    
def lessen_dic(dic_a,dic_b):
    dic = {}
    for key in dic_a.keys():
        dic[key] = dic_a[key] - dic_b.get(key,float(0.000))
    return dic
    
        
 
#定义写入EXCEL函数
def excel_write(file_name,dic_data):
    workbook = xlwt.Workbook(encoding='utf8')
    sheet = workbook.add_sheet('sheet1')
    row = 0
    for key,value in dic_data.items():
        sheet.write(row,0,key)
        sheet.write(row,1,value)
        row += 1
    workbook.save(file_name)
    return 200
    


#定义新的写入EXCEL函数。写入四列值
def excel_write_new(file_name,jh_dic,zhunzhi_dic,chazhi_dic):
    workbook = xlwt.Workbook(encoding='utf8')
    sheet = workbook.add_sheet('sheet1')
    row = 0
    for key in jh_dic.keys():
        sheet.write(row,0,key) #用户名
        sheet.write(row,1,jh_dic[key]) #聚合手机充值 
        sheet.write(row,2,zhunzhi_dic[key]) #网银充值总额
        sheet.write(row,3,chazhi_dic[key]) #差值
        row += 1
    workbook.save(file_name)


if __name__ == "__main__":
    xlxs_files = [ 'rb.xls','wy.xls']
    sum_dic_lst = []
    for xlxs_file in xlxs_files:
        #print xlxs_file
        lst_dict = read_excel(xlxs_file)
        result_dic = cre_dict(lst_dict)
        sum_dic_lst.append(result_dic)
    #print sum_dic_lst
    chuzhi_sum_dic = count_dic(sum_dic_lst)
    #print chuzhi_sum_dic #用户与充值与字典对应
    
    #最终充值金额写入EXCEL
    #excel_write('/tmp/chuzhi.xls',chuzhi_sum_dic)
    jh_lst_dic = read_excel('jh.xls')
    jh_result_dic = cre_dict(jh_lst_dic) #用户与充值的字典对应
    chazhi_dic = lessen_dic(jh_result_dic,chuzhi_sum_dic)

    excel_write_new('sum_new.xls',jh_result_dic,chuzhi_sum_dic,chazhi_dic)
    
    #print chazhi_dic
    #for k,v in chazhi_dic.items():
    #    print "%s,%4.2f" %(k,v)
    #最终差额写入EXCEL文件
    #stats = excel_write('/tmp/sum.xls',chazhi_dic)
    
    

