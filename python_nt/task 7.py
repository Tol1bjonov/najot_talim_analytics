#                                              HOMEWORK
#   1-savol
# def bankomat():
#     balans = 100000
#     while True:
#         try:
#             summa=int(input('Summani kiriting: '))
#             if balans == 0:
#                 print('Kartada pul mavjud emas!')
#                 break
#             if summa <= 0:
#                 raise TypeError('Notugri summa!')
#             if summa > balans:
#                 raise IndexError('Mablag‘ yetarli emas')
#             else:
#                 balans=balans - summa
#                 print(f'{summa} som pul yechildi /n Qoldi: {balans} som')
#         except ValueError:
#             print('Son kiriting!')
#         except TypeError as t:
#             print(t)
#         except IndexError as i:
#             print(i)
# bankomat(

#    2-Savol
# def juft_toq():
#     while True:
#         try:
#             n=int(input('Son kiriting chiqish uchun(0): '))
#             if n == 0:
#                 print('Xayr')
#                 break
#             if n%2==0:
#                 print('Juft')
#             if n%2!=0:
#                 print('Toq')
#         except ValueError:
#             print('Son kiriting!')
# juft_toq()

#  3-savol
# def password():
#     while True:
#         try:
#             parol = input('Parolni kiriting: ')
#             if len(parol) < 8:
#                 raise TypeError('Kamida 8 ta belgi kerak! ')
#             else:
#                 print('Parol saqlandi!')
#                 break
#         except TypeError as e:
#             print(e)
# password()

#  4-savol
def nums():
    while True:
        try:
            count=0
            nums=str(input('Sonlarni kiriting: '))
            num=nums.split(',')
            for i in num:
                count+=int(i)
            print(count)
            break
        except ValueError:
            print('Faqat sonlar kiriting!')
nums()








