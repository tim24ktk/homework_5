from random import randint


# #   Создайте программу для игры с конфетами человек против человека.
# #   Условие задачи: На столе лежит 117 конфета.
# #   Играют два игрока делая ход друг после друга.
# #   Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# #   Все конфеты оппонента достаются сделавшему последний ход.
# #
# # a) Добавьте игру против бота

def read_data(line: str) -> str:
    """
    функция получения данных от пользователя
    :param line: str
    :return: str
    """
    print(line)
    gamer_name = input('-> ')
    return gamer_name


def player_with_player():
    total_objects = 28
    player_number = randint(1, 2)
    winner = 0
    first_player = read_data('Введите свое имя в игре: ')
    second_player = read_data('Введите свое имя в игре: ')

    if player_number == 1:
        first = first_player
        second = second_player
    else:
        first = second_player
        second = first_player

    print(f'Первый ход делает {first}')

    while total_objects > 0:
        if winner == 0:
            print(f'{first} твой ход! Ты можешь взять не больше 28 конфет!')
            first_move = int(input('-> '))

            if first_move > total_objects or first_move > 28:
                print(f'{first} ввел недопустимое значение! Попробуйте снова!')

            total_objects -= first_move

            if total_objects > 0:
                print(f'Осталось еще {total_objects} конфет!')
                winner = 1
            else:
                print('Конфеты закончились!')

        if winner == 1:
            print(f'{second} твой ход! Ты можешь взять не больше 28 конфет!')
            second_move = int(input('-> '))

            if second_move > total_objects or second_move > 28:
                print(f'{second} ввел недопустимое значение! Попробуйте снова!')

            total_objects -= second_move

            if total_objects > 0:
                print(f'Осталось еще {total_objects} конфет!')
                winner = 1
            else:
                print('Конфеты закончились!')

    if winner == 1:
        print(f'{second} победил!')
    if winner == 0:
        print(f'{first} победил!')


player_with_player()
