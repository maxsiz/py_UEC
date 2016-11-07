# -*- coding: cp1251 -*-
# разделение реестра пополнений
import subprocess as sp
import fnmatch 
import os
import sys
if len(sys.argv)==4:
   file1 = sys.argv[1] #реестр, записи которого нужно исключить из полного
   file2 = sys.argv[2] #полный реестр
   file3 = sys.argv[2] #реестр перечислений для проверки
else:
   print (len(sys.argv))
   print ('wrong params number ',len(sys.argv), ' , usage: reestr_dev.py file1 file2')
   sys.exit
#нужно получить список пкарт из первого файла
cards_file1_ls =[card.split(';')[4] for card in open(file1)]
#нужно получить список карт из файла 3 (ездят)
cards_file3_ls =[card.split(';')[4] for card in open(file3)]
CF3=set(cards_file3_ls)
CF3.discard('')
print (len(CF3))

res_file = open('file2'+'_new', 'w') #новый файл реестра пополнений
res_file.write ('ORGANIZATIONID;INN;BIC;MIFAREUID;TRANSPORTCARDID;TICKETID;AMOUNT'+'\n')
for str1 in open(file2): #цикл по полному файлу реестра пополнений
    if  str1.split(';')[4] not in cards_file1_ls: #если карты нет в списке из первого файла , то строку пишем в новый файл
        if  str1.split(';')[4]  in CF3: #дополнительно проверим, что карта есть в списке из файла3
            res_file.write(str1)

                        