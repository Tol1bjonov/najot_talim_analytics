#Puzzle 1
# def devision():
#     try:
#         a=int(input('Birinchi sonni kiriting: '))
#         b = int(input('Ikkinchi sonni kiriting: '))
#         print(f'{a}/{b}= {a/b}')
#     except ZeroDivisionError:
#         print('0 ga bolib bolmaydi!')
#     except ValueError:
#         print('Faqat raqam kirita olasiz!')
# devision()


#Puzzle 2
# numbers=[10,20,30,40,50]
# def find_n_b_index():
#     try:
#         index=int(input('Index kiriting: '))
#         print(numbers[index])
#     except ValueError:
#          print('Faqat raqam kirita olasiz!')
#     except IndexError:
#         print('Bunday index yoq!')
# find_n_b_index()

#Puzzle 3
# while True:
#     try:
#         a=int(input('Son kiriting: '))
#         if a<=0:
#             raise TypeError('Musbat son kirita olasiz')
#
#         print('Rahmat')
#         break
#     except ValueError:
#           print('Faqat raqam kirita olasiz!')
#     except TypeError as t:
#         print(t)

#Puzzle 4
# def get_month():
#     while True:
#         try:
#             m = int(input('Oy raqamini kiriting: '))
#             if m < 1 or m > 12:
#                 raise TypeError('Bunday oy yo‘q!')
#             print('Qabul qilindi!')
#             break
#         except ValueError:
#             print('Faqat raqam kiriting!')
#         except TypeError as t:
#             print(t)
# get_month()

#Puzzle 5
def score():
    while True:
        try:
            s=int(input('Ball kiriting: '))
            if s < 0:
                raise TypeError('Musbat son kirita olasiz')
            if s not in range(1, 101):
                raise IndexError('Notugri qiymat')
            else:
                print('Qabul qilindi!')
                break
        except ValueError:
            print('Son kiriting!')
        except TypeError as t:
            print(t)
        except IndexError as i:
            print(i)
score()