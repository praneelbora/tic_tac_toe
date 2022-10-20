theboard = { '1' : ' ' , '2' : ' ' , '3' : ' ' ,
             '4' : ' ' , '5' : ' ' , '6' : ' ' ,
             '7' : ' ' , '8' : ' ' , '9' : ' '}
board_keys = []

for key in theboard:
    board_keys.append(key)


def actualboard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def tictactoe():

    turn = 'X'
    count = 0

    for i in range(10):
        actualboard(theboard)
        print("Now it's" + turn + "'s turn. Enter your desired position (1-9):")

        move = input()

        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1

        else:
            print("That place is already filled. Please choose another one.")
            continue

        if count >= 5:
            if theboard['1'] == theboard['2'] == theboard['3'] != ' ' :
                print(actualboard(theboard))
                print('\nGame over .\n')
                print(' **** ' + turn + ' won. ****')
                break

            elif theboard['4'] == theboard['5'] == theboard['6'] != ' ' :
                print(actualboard(theboard))
                print('\nGame over.\n')
                print(' **** ' + turn + ' won. ****')
                break
            
            elif theboard['7'] == theboard['8'] == theboard['9'] != ' ' :
                print(actualboard(theboard))
                print('\nGame over.\n')
                print(" **** " + turn + " won. ****")
                break

            elif theboard['1'] == theboard['4'] == theboard['7'] != ' ' :
                actualboard(theboard)
                print('\nGame over.\n')
                print(" **** " + turn + " won. ****")
                break

            elif theboard['2'] == theboard['5'] == theboard['8'] != ' ' :
                actualboard(theboard)
                print('\nGame over.\n')
                print(" **** " + turn + " won. ****")
                break

            elif theboard['3'] == theboard['6'] == theboard['9'] != ' ' :
                print(actualboard(theboard))
                print('\nGame over.\n')
                print(" **** " + turn + " won. ****")
                break

            elif theboard['1'] == theboard['5'] == theboard['9'] != ' ' :
                print(actualboard(theboard))
                print('\nGame over.\n')
                print(" **** " + turn + " won. ****")
                break

            elif theboard['3'] == theboard['5'] == theboard['7'] != ' ' :
                print(actualboard(theboard))
                print('\nGame over.\n')
                print(" **** " + turn + " won. ****")
                break

        if count == 9:
            print('\nGame over.\n')
            print("It's a tie")

        if turn == "X":
            turn = 'O'

        else:
            turn = 'X'

    restart = input("Do you want to play again?(y/n)")
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            theboard[key] = " "

        tictactoe()

tictactoe()
actualboard()