# -*- coding: cp1251 -*-
# Для замены новых карт на старую
# usage: settle_canhge_new_cards.py file2 file3 file4
# !!!!!!!!!!!!где file1-файл C:\Users\Sizykh\python_example\settle_change_new_cards.pyс номерами карт,котороые ездят, но не пополнялись - перевыпущенные (один номер в строке) НЕ ИСПОЛЬЗУЕТСЯ.
# file2 - файл с -соответствием! перевыпущенная карта;старая карта (одна пара в строке, разделитель ";")
# file3 - реестр перечислений, в котром нужно сделать подмену
# file4 - текущий реестр пополнений для сверки 
# C:\Share_transport\LINK\AISVTK\perevipusk\perevip.csv 
import subprocess as sp
import fnmatch 
import os
import sys
#получим список параметров  из командной строки, если он передан
if len(sys.argv)==4:
   #file1 = sys.argv[1]
   file2 = sys.argv[1]
   file3 = sys.argv[2]
   file4 = sys.argv[3]
else:
   print (len(sys.argv))
   print ('wrong params number ',len(sys.argv), ' , usage: settle_canhge_new_cards.py file2 file3 file4')
   sys.exit
#1. first buld list of used cards 
used_cards_ls =[card.split(';')[4] for card in open(file3)]
UC = set(used_cards_ls)
UC.discard('')
print ('Set of used card ', len(UC), ' is builded from ', len(used_cards_ls))
charged_cards_ls =[card.split(';')[4] for card in open(file4)]
CHC = set(charged_cards_ls)
CHC.discard('')
print ('Set of charged card ', len(CHC), ' is builded from ', len(charged_cards_ls))
#charged_cards_ls = [charge_card.split(';')[4] for charge_card in open(file4)]
card_ls = list(UC-CHC)
#card_ls=[card.rstrip() for card in open(file1)]
print ('List of used  uncharged cards is builded: ', len(card_ls))
#charged_not_used_card_ls = list(CHC-UC)
#card_ls=[card.rstrip() for card in open(file1)]
#print ('List of charged_not_used_card is builded: ', len(charged_not_used_card_ls))

#2. buld 
log_file = open('log_change2.txt','w') #новый файл
exch_dct = {}
for card in card_ls:#цикл по списку карт, которые ездят, но не пополнены(перевыпущенные)
    print (card, end='' )
    log_file.write(card)
    for exch_str in open(file2):#цикл по файлу соответствия перевыпусков для заполнения словаря
        #print (exch_str.rstrip())
        if  int(card) == int(exch_str.split(';')[0]) and int(exch_str.split(';')[0]) > int(exch_str.split(';')[1]):
            exch_dct[exch_str.split(';')[0]]=exch_str.split(';')[1].rstrip()
            print(' -added with ',exch_str.split(';')[1].rstrip())
            log_file.write(' -added with '+ exch_str.split(';')[1].rstrip()+'\n')
            break 
        elif int(card)== int(exch_str.split(';')[1]) and int(exch_str.split(';')[1]) > int(exch_str.split(';')[0]):
            exch_dct[exch_str.split(';')[1]]=exch_str.split(';')[0].rstrip()
            print(' -added with ',exch_str.split(';')[0].rstrip())
            log_file.write(' -added with '+exch_str.split(';')[1].rstrip()+'\n')
            break
    else:
        #карта не найдена среди перевыпущенных
        print ('-no match')   
        log_file.write('-no match'+'\n')
        #print(exch_str.split(';')[0])
print ('Всего в словарь добавлено ', len(exch_dct))
log_file.write('Всего в словарь добавлено '+ str(len(exch_dct))+'\n')
#теперь собствено подмена  новой карты на старую для file3, но сначала проверим, что "старые карты" пополнены на текущий месяц
#print (exch_dct.values(), len(exch_dct.values()))
not_charged_ls =[]
for old_card in exch_dct.values():#цикл по значениям словаря             
    if  old_card in CHC: #проверка на вхождение во множество пополненных карт
        print (old_card, ' is charged - OK') 
        log_file.write(old_card+ ' is charged - OK'+'\n')
    else:                        
        not_charged_ls.append(old_card)
j=0
if  len(not_charged_ls)==0: #if all old cards are charged, do replace
    print ('Replacing in ', file3,' ...')
    res_file = open(file3+'_new2','w') #новый файл
    #res_file.write('ORGANIZATIONID;INN;BIC;MIFAREUID;TRANSPORTCARDID;TICKETID;AMOUNT\n')
    for f3_st in open(file3):  #цикл по файлу исходного реестра перечислений
        #если в текущей строке файла перечислений есть "новая" карта, то её нужно заменить на старую
        if  f3_st.split(';')[4] in exch_dct.keys():
            res_file.write(f3_st.replace(f3_st.split(';')[4], exch_dct.get(f3_st.split(';')[4])))
            j +=1
        else:
            res_file.write(f3_st)
    print ('Card replacing is Done... ',str(j),' ',res_file.name)
    #теперь заменим сумму, если старая карта ездила
    old_used_card_ls=[]
    for old_card in exch_dct.values():#цикл по значениям словаря с перевыпущеными картами             
        if  old_card in UC: #проверка на вхождение во множество ездющих карт
            old_used_card_ls.append(old_card)
    print (' List of old_used_card_ls - OK '+str(len(old_used_card_ls))) 
    log_file.write(' List of old_used_card_ls - OK '+str(len(old_used_card_ls))+'\n')
    old_used_card_ls.sort()
    #log_file.writelines(old_used_card_ls)
    res_file.close()
    res_file = open(file3+'_new2')
    res_file3 = open(file3+'_new3','w') #новый файл
    res_file3.write('ORGANIZATIONID;INN;BIC;MIFAREUID;TRANSPORTCARDID;TICKETID;AMOUNT'+'\n')
    j=0
    for f3_st in res_file:  #цикл по файлу реестра перечислений c уже подмененной картой
    #если в текущей строке файла  есть карта из фильра, то нужно сумму уменьшить в 2 раза
        if  f3_st.split(';')[4] in old_used_card_ls:
            f3_ls = f3_st.rstrip().split(';')
            log_file.write(f3_ls[4]+';'+f3_ls[6]+';'+str(int(f3_ls[6])//2)+'\n')
            f3_ls[6] = int(f3_ls[6])//2
            res_file3.write(f3_ls[0]+';'+f3_ls[1]+';'+f3_ls[2]+';'+f3_ls[3]+';'+f3_ls[4]+';'+f3_ls[5]+';'+str(f3_ls[6])+'\n')
            j +=1
        else:
            res_file3.write(f3_st)
    print ('Done... ',str(j),' ',res_file3.name)
else:
    print (not_charged_ls, ' list of not charged OLD cards in current month')
    not_charged_ls = [sstr +'\n' for sstr in not_charged_ls]
    not_charged_ls.sort()
    log_file.writelines( not_charged_ls)
    log_file.write('\n'+' list of not charged OLD cards in current month')                                            
#теперь исключим из исходного реестра пополненений те карты, которых нет в обновленом реестре списаний (res_file3)
res_file3.close()
res_file3 = open(file3+'_new3') #открываем заново новый файл реестра списаний в  режиме просмотра
final_card_ls = [card.split(';')[4] for card in res_file3 if len(card.split(';')[0])<5]
ls = [int(card.split(';')[6]) for card in open(file3+'_new3') if len(card.split(';')[0])<5]
control_sum = sum(ls)
print (control_sum)
FC = set(final_card_ls)
FC.discard('')
log_file.write('Карт в новом файле перечислений: '+str(len(FC))+'\n')
log_file.write('Контрольная сумма из нового файла перечислений :'+str(control_sum)+'\n')
#теперь множество FC содержит список уникальных карт, по которым будет списание в этом месяце
control_sum2=0
k=0
res_file4 = open(file4+'_new4', 'w') #новый файл реестра пополнений
res_file4.write ('ORGANIZATIONID;INN;BIC;MIFAREUID;TRANSPORTCARDID;TICKETID;AMOUNT'+'\n')
for str1 in open(file4): #цикл по старому файлу реестра пополнений
    if  str1.split(';')[4] in FC: #если карта   есть в  новом реестре списаний, то строку пишем в новый файл
        res_file4.write(str1)
        k +=1
        control_sum2 += int(str1.split(';')[6])
log_file.write('Строк в новом файле пополнений: '+str(k)+'\n')
log_file.write('Контрольная сумма из нового файла пополнений :'+str(control_sum2) +'\n')
