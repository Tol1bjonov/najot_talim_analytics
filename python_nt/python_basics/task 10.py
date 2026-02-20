# 1.	Faqat 5 dan katta sonlarni ajrat. Ularning kubini (x³) hisobla. Natijani list ko‘rinishida chiqar.
# sonlar = [3, 7, 2, 9, 12, 5, 18, 4]
# result = list(map(lambda x: x**3, filter(lambda x: x > 5, sonlar)))
# print(result)

# 2 Faqat 5 ga bo‘linadigan sonlarni ol. Ularni 2 ga ko‘paytir. Oxirida faqat 50 dan kichik bo‘lganlarini qoldir.
# sonlar = [10, 15, 20, 25, 30, 35, 40]
# result = list(
#     filter(lambda x: x < 50,
#         map(lambda x: x*2,
#             filter(lambda x: x % 5 == 0, sonlar)
#         )
#     )
# )
# print(result)

#3 Faqat kvadrat ildizi butun son bo‘lganlarini qoldir. Ularning ildizini top. Natijani string ko‘rinishda chiqar:
# sonlar = [4, 9, 16, 25, 36, 49, 64]
# result = [str(int(x**0.5)) for x in sonlar]
# print(result)

#4 3 harfdan uzun so‘zlarni ajrat. Oxirgi harfini olib tashla. Hammasini katta harfga o‘tkaz.
# sozlar = ["python", "sql", "data", "ai", "analysis", "ml"]
# result = list(
#     map(lambda w: w[:-1].upper(),
#         filter(lambda w: len(w) > 3, sozlar)
#     )
# )
# print(result)
