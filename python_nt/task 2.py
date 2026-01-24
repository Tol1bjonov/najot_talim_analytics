#                          PUZZLE 1
# kod = "admin"
# urinishlar = 3
# while True:
#     savol=input("Parolni kiriting: ")
#     if savol==kod:
#         print("Xush kelibsiz!")
#         break
#     else:
#         urinishlar=urinishlar-1
#         if urinishlar==0:
#             print("Bloklandi!")
#             break
#         else:
#             print(f"Xato! {urinishlar} ta imkoniyat qoldi!")


#                            PUZZLE 2
# umumiy = 0
# while True:
#     try:
#         a = float(input("# "))
#         if a > 0:
#             umumiy = umumiy + a
#         else:
#             print(f"Umumiy yigindi: {umumiy}")
#             break
#     except:
#         print("Iltimos faqat raqam kiriting!")


#                             PUZZLE 3
# hisob = 1000000
# while True:
#     try:
#         summa = int(input("Qancha pul yechib olishni xoxlaysiz? "))
#         if summa == 0:
#             print("Jarayon yakunlandi!")
#             break
#         else:
#             if summa < 0:
#                 print("Xato summa!")
#             elif summa > hisob:
#                 print("Balans yetarli emas" )
#             elif summa < hisob and summa > 0:
#                 hisob=hisob-summa
#                 print(f"Hisobingizdan {summa} so`m yechildi. Balans: {hisob} so`m")
#
#     except:
#         print("Iltimos faqat raqam kiriting!")

