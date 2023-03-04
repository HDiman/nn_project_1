# Num 1
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(self.name + " is barking!")
#
# dog1 = Dog("Rex", 3)
# dog1.bark()
#
# print(dog1.name)

# Num 2
# import random
#
# print("Добро пожаловать в игру угадай число!")
# print("Я загадаю число в диапазоне от 1 до 100, а вы должны отгадать его.")
#
# number = random.randint(1, 100)
# attempts = 0
#
# while True:
#     guess = int(input("Введите число: "))
#     attempts += 1
#
#     if guess == number:
#         print(f"Поздравляю, вы угадали число за {attempts} попыток!")
#         break
#     elif guess < number:
#         print("Загаданное число больше. Попробуйте еще раз.")
#     else:
#         print("Загаданное число меньше. Попробуйте еще раз.")


# def my_decorator(func):
#     def wrapper():
#         print("До вызова функции.")
#         func()
#         print("После вызова функции.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Привет!")
#
# say_hello()
#
# my_decorator(say_hello())