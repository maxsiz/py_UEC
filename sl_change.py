#строим словарь с ключами из номеров перевыпущенных карт
print ('строим словарь с ключами из номеров перевыпущенных карт - .. ', end='')
card_change_sl = {data.rstrip().split(';')[0][10:] #com1
                  :data.rstrip().split(';')[1][10:]  
                 for data in open('change.csv', encoding='cp1251')}
print(card_change_sl)
print ('ok '+ str(len(card_change_sl)))

