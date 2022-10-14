from random import randint
from itertools import groupby

def task1():
    # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

    text = 'Hello абв, Worабвld!'
    my_list = list(filter(lambda x: 'абв' not in x , text.split()))
    print(' '.join(my_list))

def task2():
    # Создайте программу для игры с конфетами человек против человека.

    # Условие задачи: На столе лежит 2021 конфета. 
    # Играют два игрока делая ход друг после друга. 
    # Первый ход определяется жеребьёвкой. 
    # За один ход можно забрать не более чем 28 конфет. 
    # Все конфеты оппонента достаются сделавшему последний ход. 
    # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

    bank = 2021
    first_take = bank - bank // 29 * 29
    print(f'Для победы первому игроку нужно взять {first_take} конфет\n')

    def input_take(name):
        candy = int(input(f'Игрок {name}, введите количество конфет, от 1 до 28: '))
        while candy < 1 or candy > 28:
            candy = int(input(f'Игрок {name}, введите количество конфет, от 1 до 28: '))
        return candy

    def print_move(name, candy_counter, counter, value):
        print(f'Ходил игрок {name}, он взял {candy_counter} конфет, '
              f'теперь у него {counter} конфет. На столе осталось {value} конфет.')

    player_first = input('Введите имя первого игрока: ')
    while len(player_first) == 0:
        player_first = input('Введите имя первого игрока повторно: ')
    player_second = input('Введите имя второго игрока: ')
    while len(player_second) == 0 or player_second == player_first:
        player_second = input('Введите имя второго игрока повторно: ')

    priority = randint(1,2)
    if priority == 1:
        print(f'Первым ходит игрок {player_first}')
    else:
        print(f'Первым ходит игрок {player_second}')
    counter_first = 0
    counter_second = 0
    while bank > 28:
        if priority == 1:
            candy_counter = input_take(player_first)
            counter_first += candy_counter
            bank -= candy_counter
            priority = 2
            print_move(player_first, candy_counter, counter_first, bank)
        else:
            candy_counter = input_take(player_second)
            counter_second += candy_counter
            bank -= candy_counter
            priority = 1
            print_move(player_second, candy_counter, counter_second, bank)
    if priority == 1:
        print(f'Игрок {player_first} победил')
    else:
        print(f'Игрок {player_second} победил')

def task3():
    # Создайте программу для игры в ""Крестики-нолики"".

    board = list(range(1,10))

    def draw_board(board):
        print('-' * 13)
        for i in range(3):
            print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], "|")
            print('-' * 13)

    def take_input(player_token):
        valid = False
        while not valid:
            player_answer = input('Выберите клетку для ' + player_token + '? ')
            try:
                player_answer = int(player_answer)
            except:
                print('Некорректный ввод. Введите число от 1 до 9.')
                continue
            if player_answer >= 1 and player_answer <= 9:
                if(str(board[player_answer - 1]) not in 'XO'):
                    board[player_answer - 1] = player_token
                    valid = True
                else:
                    print('Эта клетка уже занята!')
            else:
                print('Некорректный ввод. Введите число от 1 до 9.')

    def check_win(board):
        win_coord = ((0, 1, 2), (3, 4, 5),
                     (6, 7, 8), (0, 3, 6),
                     (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
        return False

    def main(board):
        counter = 0
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                take_input('X')
            else:
                take_input('O')
            counter += 1
            if counter > 4:
                tmp = check_win(board)
                if tmp:
                    draw_board(board)
                    print(tmp, 'выиграл!')
                    win = True
                    break
            if counter == 9:
                draw_board(board)
                print('Ничья!')
                break
    main(board)

def task4():
    # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

    def compress(text):
        for char, same in groupby(text):
            count = sum(1 for _ in same)
            yield char if count == 0 else str(count) + char

    def recovery(text_compress):
        decode = ''
        count = ''
        for char in text_compress:
            if char.isdigit():
                count += char
            else:
                decode += char * int(count)
                count = ''
        return decode

    text = 'HaaaaaaaCCCCCCgHHHHHqqqqqCCCCa'
    text_compress = ''.join(compress(text))
    print(f'Введённая строка: ' + text)
    print(f'Сжатая строка: {text_compress}')
    print(f'Востановленная строка: {recovery(text_compress)}')

    # text_recovery = text_compress.replace(' ', '')
    # print(text_recovery)




task1()
# task2()
# task3()
# task4()
