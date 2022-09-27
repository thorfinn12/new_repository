# my_name = 'luka'
# my_surname = 'chkhitunidze'
# my_age = 19
# my_sentence = "my name {0} my age {2} my surname  {1}".format(my_name,my_age,my_surname)

# print(my_sentence)

#--------------------------------------------

# my_fullnamem = 'luka chkhitunidze'
# if 'l' in my_fullnamem:
#     print('sheicavs l-s')
# else:
#     print('ar sheicavs l-s')

#-----------------------------------------------

#------------------------\
#    input,output
#------------------------/

# my_name = input('enter your name: luk')
# print("chemi saxelia" + " " + my_name)

#-----------------------------------------

# my_age = 19
#
# my_age += 3
#
# print(my_age)
#------------------დავალება ერთი-----------------------

# user_name = input('რა გქვია: ')
#
# user_lastname = input('რა გვარი ხარ: ')
#
# user_age = int(input('რამდენი წლის ხარ: '))
#
#
# print('შენი სახელია {2},შენი გვარია {1} და ხარ {0} წლის'.format(user_age,user_lastname,user_name))
#
# years = input("ჩაწერე წელი: ")
#
# user_new_age = int(user_age) + int(years)
#
# print("ხუთი წლის შემდეგ შენ იქნები {} წლის".format(user_new_age))

# --------------savarjisho 2----------------------------------

# num1 = int(input('დაწერე რაიმე რიცხვი: '))

# num2 = int(input('დაწერე კიდევ სხვა რომელიმე რიცხვი: '))
#
# multiplay = num1 * num2
#
# if multiplay > 100:
#     print('product')
# else:
#     print('u lose')

#input,%,if,+=

num1 = int(input("შემოიტანე პირველი რიცხვი: "))

num2 = int(input("შემოიტანე მეორე რიცხვი: "))

num3 = int(input("შემოიტანე მესამე რიცხვი: "))

total = 0


if num1 % 2 == 1:
    total += num1


if num2 % 2 == 1:
    total += num2

if num3 % 2 == 1:
    total += num3
 


print(total)

