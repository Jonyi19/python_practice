the_board = {'top-L':' ','top-M':' ','top-R':' ',
              'mid-L': ' ','mid-M': ' ','mid-R': ' ',
              'low-L': ' ' ,'low-M': ' ' ,'low-R': ' ' }

def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'] )
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'] )
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] )

def victory(board,turn):
    if board['top-L'] == board['top-M'] == board['top-R']:
        return print(turn + 'の勝利') , True
    else:
        return
        



turn = 'X'
key = list(the_board.keys())
for i in range(9):
    print_board(the_board)
    print(turn + 'の番です。どこに打ちますか')
    while True:
        move = input()
        if move not in key:
            print('不正な値です。以下から選択して下さい')
            print(str(key))
        else:
            key.remove(move)
            break

    the_board[move] = turn
    if victory(the_board,turn):
        break
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    

print_board(the_board)
