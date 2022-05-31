from random import randint

#▄

filler = ' '
apple = '•'



def board_creator():
    board_array = []
    for i in range(10):
        for j in range(10):
            board_array[i][j].append(filler)
    return board_array

def board_printer(board_array):
    for i in range(10):
        for j in range(10):
            print('[' + board_array[i][j] + ']', end='')
        print('')

def apple_setter(board_array):
    x = randint(0, 9)
    y = randint(0, 9)
    board_array[x][y] = apple
    return board_array

def gra():
    win_condition = False
    board_array = board_creator()
    while not win_condition:
        board_array = apple_setter(board_array)
        board_printer(board_array)
        move = input()


gra()