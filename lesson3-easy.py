# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"

# def function(name, age, city):
#     print('{}, {} год(а), проживает в городе {}'.format(name, age, city))
# name = input('Введите, пожалуйста, Ваше имя ')
# age = input('Введите год Вашего рождения ')
# city = input('Город Вашего проживания ')
# function(name, age, city)
# print()


# # Задание - 2
# # Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

# import random
# a = random.randint(-10, 5)
# b = random.randint(-10, 5)
# c = random.randint(-10, 5)
# print(a, b, c)
# def maxfunk(x, y, z):
#     m = (max(x, y, z))
#     return m
# print('Наибольшее число:', maxfunk(a, b, c))
# print()

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов
 
# def strlong(*args):
#     x = 0
#     for arg in args:
#         if len(arg) > x:
#             x = len(arg)
#             maxlen = arg
#         else:
#             pass
#     return maxlen
# name = ['г-н Чернов А.Ю.', 'претензия', '17/1', 'ответ']
# print(strlong(*name))
