# Игра 1. Угадай число.
# Правила игры. В игре присутствует 3 уровня сложности. 1 уровень предоставляет 10 попыток угадать число.
# 2 уровень 5 попыток и 3 предоставляет 3 попытке.
# В игре указываются колличество играков пользователем.
# Вводите имя игрока.

import random

number = random.randint(1, 100)
# print(number)   закомментировал чтобы игрок не видел какое число загодал компьютер

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input('Выберите уровень сложности: '))
max_count = levels[level]

user_count = int(input('Введите количество пользователей: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i}: ')
    users.append(user_name)

print(users)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('Все пользователи проиграли')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
else:
    print(f'Победитель {winner_name}')
