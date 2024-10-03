# Tic Tac Toe 3/5/24
import random


def main():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    choices = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print('Welcome to Tic Tac Toe!')
    mode = int(input('1 for single player, 2 for multiplayer: '))
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')
    while True:
        choice = input('Choose your spot (1-9): ').strip()
        while choice not in choices:
            choice = input('Invalid option: ').strip()
        printBoard(choice, board, choices, 'x')
        if mode == 2:
            if checkWin(board):
                print('x won!')
                break
            choice = input('Choose your spot (1-9): ').strip()
            while choice not in choices:
                choice = input('Invalid option: ').strip()
            printBoard(choice, board, choices, 'o')
            if checkLoss(board):
                print('o won!')
                break
        if mode == 1:
            if checkWin(board):
                print('You won! :)')
                break
            AI(board, choices)
            if checkLoss(board):
                print('You lost :(')
                break


def AI(board, choices):
    print('AI\'s Turn:')
    ai_choice = random.choice(choices)
    printBoard(ai_choice, board, choices, 'o')


def checkWin(board):
    if board[0] == 'x' and board[1] == 'x' and board[2] == 'x':
        return True
    if board[3] == 'x' and board[4] == 'x' and board[5] == 'x':
        return True
    if board[6] == 'x' and board[7] == 'x' and board[8] == 'x':
        return True
    if board[0] == 'x' and board[3] == 'x' and board[6] == 'x':
        return True
    if board[1] == 'x' and board[4] == 'x' and board[7] == 'x':
        return True
    if board[2] == 'x' and board[5] == 'x' and board[8] == 'x':
        return True
    if board[0] == 'x' and board[4] == 'x' and board[8] == 'x':
        return True
    if board[6] == 'x' and board[4] == 'x' and board[2] == 'x':
        return True


def checkLoss(board):
    if board[0] == 'o' and board[1] == 'o' and board[2] == 'o':
        return True
    if board[3] == 'o' and board[4] == 'o' and board[5] == 'o':
        return True
    if board[6] == 'o' and board[7] == 'o' and board[8] == 'o':
        return True
    if board[0] == 'o' and board[3] == 'o' and board[6] == 'o':
        return True
    if board[1] == 'o' and board[4] == 'o' and board[7] == 'o':
        return True
    if board[2] == 'o' and board[5] == 'o' and board[8] == 'o':
        return True
    if board[0] == 'o' and board[4] == 'o' and board[8] == 'o':
        return True
    if board[6] == 'o' and board[4] == 'o' and board[2] == 'o':
        return True


def printBoard(choice, board, choices, player):
    if choice == '1':
        board[0] = player
        choices.remove('1')
    elif choice == '2':
        board[1] = player
        choices.remove('2')
    elif choice == '3':
        board[2] = player
        choices.remove('3')
    elif choice == '4':
        board[3] = player
        choices.remove('4')
    elif choice == '5':
        board[4] = player
        choices.remove('5')
    elif choice == '6':
        board[5] = player
        choices.remove('6')
    elif choice == '7':
        board[6] = player
        choices.remove('7')
    elif choice == '8':
        board[7] = player
        choices.remove('8')
    elif choice == '9':
        board[8] = player
        choices.remove('9')
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')


if __name__ == '__main__':
    main()
