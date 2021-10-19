
ik=''
while len(ik)!=11 or ik.isdigit()!=True:
    try:
        ik=input('Введите личный код: ')
    except ValueError:
        print('Ошибка с данными')
print('Isikukoodi anaüüs'.center(50,'-')) 
ik_list=list(ik)
if int(ik_list[0]) not in [1,2,3,4,5,6]:
    print(f'{ik_list[0]} - неправильно')
#aasta ik_list[1], ik_list[2]
#kuu ik_list[3], ik_list[4]
#päev ik_list[5], ik_list[6]
#50206273713
if ik_list[0] == '3':
    print('Вы мужчина.')
    print(f'Вы родились в ''19'+ik_list[1]+ik_list[2])
elif ik_list[0] == '4':
    print('Вы женщина.')
    print(f'Вы родились в ''19'+ik_list[1]+ik_list[2])
elif ik_list[0] == '5':
    print('Вы мужчина.')
    print(f'Вы родились в ''20'+ik_list[1]+ik_list[2])
elif ik_list[0] == '6':
    print('Вы женщина.')
    print(f'Вы родились в ''20'+ik_list[1]+ik_list[2])
if ik_list[3]=='0' or '1' and ik_list[4]!='0':
    if ik_list[3]=='0' and ik_list[4]=='1':
        print('Вы родились в январе.')
    elif ik_list[3]=='0' and ik_list[4]=='2':
        print('Вы родились в феврале.')
    elif ik_list[3]=='0' and ik_list[4]=='3':
        print('Вы родились в марте.')
    elif ik_list[3]=='0' and ik_list[4]=='4':
        print('Вы родились в апреле.')
    elif ik_list[3]=='0' and ik_list[4]=='5':
        print('Вы родились в мае.')
    elif ik_list[3]=='0' and ik_list[4]=='6':
        print('Вы родились в июне.')
    elif ik_list[3]=='0' and ik_list[4]=='7':
        print('Вы родились в июле.')
    elif ik_list[3]=='0' and ik_list[4]=='8':
        print('Вы родились в августе.')
    elif ik_list[3]=='0' and ik_list[4]=='9':
        print('Вы родились в сентябре.')
    elif ik_list[3]=='1' and ik_list[4]=='0':
        print('Вы родились в октябре.')
    elif ik_list[3]=='1' and ik_list[4]=='2':
        print('Вы родились в ноябре.')
    elif ik_list[3]==0 and ik_list[4]==1:
        print('Вы родились в декабре.')
    elif ik_list[3]==0 and ik_list[4]==0:
        print('Неверный личный код.')
else:
    print('Неверный личный код.')
if ik_list[5]=='0' or '1' or '2' or '3' and ik_list[6]=='0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9':
    if ik_list[5]=='0' and ik_list[6]=='1':
        print('Вы родились 1-го числа.')
    elif ik_list[5]=='0' and ik_list[6]=='2':
        print('Вы родились 2-го числа.')
    elif ik_list[5]=='0' and ik_list[6]=='3':
        print('Вы родились 3-го числа.')
    elif ik_list[5]=='0' and ik_list[6]=='4':
        print('Вы родились 4-го числа.')
    elif ik_list[5]=='0' and ik_list[6]=='5':
        print('Вы родились 5-го числа.')
    elif ik_list[5]=='0' and ik_list[6]=='6':
        print('Вы родились 6-го числа.')
    elif ik_list[5]=='0' and ik_list[6]=='7':
        print('Вы родились 7-го числа.')
    elif ik_list[5]=='0' and ik_list[6]=='8':
        print('Вы родились 8-го числа.')
    elif ik_list[5]=='0' and ik_list[6]=='9':
        print('Вы родились 9-го числа.')
    elif ik_list[5]=='1' and ik_list[6]=='0':
        print('Вы родились 10-го числа.')
    elif ik_list[5]=='1' and ik_list[6]=='1':
        print('Вы родились 11-го числа.')
    elif ik_list[5]=='1' and ik_list[6]=='2':
        print('Вы родились 12-го числа.')
    elif ik_list[5]=='1' and ik_list[6]=='3':
        print('Вы родились 13-го числа.')
    elif ik_list[5]=='1' and ik_list[6]=='4':
        print('Вы родились 14-го числа.')
    elif ik_list[5]=='1' and ik_list[6]=='5':
        print('Вы родились 15-го числа.')
    elif ik_list[5]=='1' and ik_list[6]=='6':
        print('Вы родились 16-го числа.')
    elif ik_list[5]=='1' and ik_list[6]=='7':
        print('Вы родились 17-го числа.')
    elif ik_list[5]=='1' and ik_list[6]=='8':
        print('Вы родились 18-го числа.')
    elif ik_list[5]=='1' and ik_list[6]=='9':
        print('Вы родились 19-го числа.')
    elif ik_list[5]=='2' and ik_list[6]=='0':
        print('Вы родились 20-го числа.')
    elif ik_list[5]=='2' and ik_list[6]=='1':
        print('Вы родились 21-го числа.')
    elif ik_list[5]=='2' and ik_list[6]=='2':
        print('Вы родились 22-го числа.')
    elif ik_list[5]=='2' and ik_list[6]=='3':
        print('Вы родились 23-го числа.')
    elif ik_list[5]=='2' and ik_list[6]=='4':
        print('Вы родились 24-го числа.')
    elif ik_list[5]=='2' and ik_list[6]=='5':
        print('Вы родились 25-го числа.')
    elif ik_list[5]=='2' and ik_list[6]=='6':
        print('Вы родились 26-го числа.')
    elif ik_list[5]=='2' and ik_list[6]=='7':
        print('Вы родились 27-го числа.')
    elif ik_list[5]=='2' and ik_list[6]=='8':
        print('Вы родились 28-го числа.')
    elif ik_list[5]=='2' and ik_list[6]=='9':
        print('Вы родились 29-го числа.')
    elif ik_list[5]=='3' and ik_list[6]=='0':
        print('Вы родились 30-го числа.')
    elif ik_list[5]=='3' and ik_list[6]=='1':
        print('Вы родились 31-го числа.')
else:
    print('Неверный личный код.')
(ik_list[0])=int(ik_list[0])
(ik_list[1])=int(ik_list[1])
(ik_list[2])=int(ik_list[2])
(ik_list[3])=int(ik_list[3])
(ik_list[4])=int(ik_list[4])
(ik_list[5])=int(ik_list[5])
(ik_list[6])=int(ik_list[6])
(ik_list[7])=int(ik_list[7])
(ik_list[8])=int(ik_list[8])
(ik_list[9])=int(ik_list[9])
k_4islo=int()
k_4islo=int(ik_list[0])*1+int(ik_list[1])*2+int(ik_list[2])*3+int(ik_list[3])*4+int(ik_list[4])*5+int(ik_list[5])*6+int(ik_list[6])*7+int(ik_list[7])*8+int(ik_list[8])*9+int(ik_list[9])*1
kon_rez=k_4islo-k_4islo//11*11
print (f'Ваше контрольное число',kon_rez)
Kur=ik_list[7]*100+ik_list[8]*10+ik_list[9]
if 1 <= Kur <= 10:
    print('Kuressaare Haigla')
elif 11<= Kur<= 19:
    print('Tartu Ülikooli Naistekliinik, Tartumaa, Tartu')
elif 21<= Kur <=220:
    print('Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla')
elif 221 <= Kur <=270:
    print('Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)')
elif 271 <= Kur <= 370:
    print('Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla')
elif 371<=Kur<=420:
    print('Narva Haigla')
elif 421<=Kur<=470:
    print('Pärnu Haigla')
elif 471<=Kur<=490:
    print('Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla')
elif 491<=Kur<=520:
    print('Järvamaa Haigla (Paide)')
elif 521<=Kur<=570:
    print('Rakvere, Tapa haigla')
elif 571<=Kur<=600:
    print('Valga Haigla')
elif 601<=Kur<=650:
    print('Viljandi Haigla')
elif 651<=Kur<=700:
    print('Lõuna-Eesti Haigla (Võru), Põlva Haigla')