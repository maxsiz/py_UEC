# -*- coding: cp1251 -*-
# Поиск ранее выданных УЭК
# usage: getuectp.py file1
import subprocess as sp
import fnmatch 
import os
import sys
if  len(sys.argv)==2:
    file1 = sys.argv[1]
else:
   print (len(sys.argv))
   print ('wrong params number ',len(sys.argv), ' , usage: '+str(sys.argv[1])+' file1')
   print(sys.argv)
   sys.exit
res_file = open('uectp'+file1, 'w') #итоговый файл
cur_file=open(file1, encoding='cp1251') #открываем отобраный файл
j = 0
k = 0

cur_file_ls = [curr_str.rstrip().split(';')[5]+';'+curr_str.rstrip().split(';')[0]+' '
                +curr_str.rstrip().split(';')[1][0] 
                #+ curr_str.rstrip().split(';')[2][0]
                +';'
                +uec_str.rstrip().split(';')[8]
                #+'snils ais'+curr_str.rstrip().split(';')[4]+'snils uec' +uec_str.rstrip().split(';')[4]
                +'\n'
                     for curr_str in cur_file 
                         for uec_str in open(r"uec_201610.csv", encoding='cp1251')
                             if  len(curr_str.rstrip().split(';'))>4 
                                  and ((curr_str.rstrip().split(';')[4] == uec_str.rstrip().split(';')[4]) 
                                 or  curr_str.rstrip().split(';')[0].upper()
                                     +curr_str.rstrip().split(';')[1].upper()
                                     +curr_str.rstrip().split(';')[2].upper()
                                     +curr_str.rstrip().split(';')[3]==uec_str.rstrip().split(';')[0].upper()
                                     +uec_str.rstrip().split(';')[1].upper()+uec_str.rstrip().split(';')[2].upper()
                                     +uec_str.rstrip().split(';')[3]
                                    )
              ]       

res_file.writelines(cur_file_ls)

#for curr_str in cur_file:
#    j +=1
#    cur_str_ls = curr_str.rstrip().split(';') #цикл по каждой строке
#    for s1 in open(r"C:\Share_transport\UEC\uec_201610.csv"):
#        print (file1+' '+str(j)+' '+str(k))
#        s1_ls=s1.rstrip().split(';')
#        k +=1
#        if  (cur_str_ls[4]==s1_ls[4]) or (cur_str_ls[0].upper()+cur_str_ls[1].upper()+cur_str_ls[2].upper()+cur_str_ls[3]==s1_ls[0]+s1_ls[1]+s1_ls[2]+s1_ls[3]):
#            res_file.write(cur_str_ls[5]+';'+cur_str_ls[0]+' '+cur_str_ls[1][0]+cur_str_ls[2][0]+';'+s1_ls[8]+'\n')
