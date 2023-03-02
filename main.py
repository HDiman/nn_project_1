import random

print("Добро пожаловать в игру угадай число!")
print("Я загадаю число в диапазоне от 1 до 100, а вы должны отгадать его.")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Введите число: "))
    attempts += 1

    if guess == number:
        print(f"Поздравляю, вы угадали число за {attempts} попыток!")
        break
    elif guess < number:
        print("Загаданное число больше. Попробуйте еще раз.")
    else:
        print("Загаданное число меньше. Попробуйте еще раз.")



