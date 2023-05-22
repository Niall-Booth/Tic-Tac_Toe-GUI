from tkinter import *
import os
import time
import random

clear = lambda: os.system('cls')

def Reset(buttons):
    for x in range(0,len(buttonsClicked)):
        buttonsClicked[x] = False
    playerOneWon = False
    playerTwoWon = False
    for x in range(0,len(buttons)): 
        buttons[x]['text'] = '-'
    for x in range(0,len(buttons)):
        buttons[x]['fg'] = 'black'
    entry.delete(0, END)
    entry.insert(0, "player one's turn")
    clear()

def Button_Click(index):
    turnOver = False
    if buttonsClicked[index] == False:
        buttonsClicked[index] = True
        buttons[index]['text'] = 'X'
        turnOver = True
        global playerOneWon
        global playerTwoWon
        playerOneWon = CheckPlayerWon('X')
        playerTwoWon = CheckPlayerWon('O')
        draw = CheckDraw(buttons)
    else:
        entry.delete(0, END)
        entry.insert(0, 'filled square try again')
        turnOver = False
        draw = False
        playerOneWon = False
        playerTwoWon = False   
    if turnOver and not playerOneWon and not playerTwoWon and not draw:
        entry.delete(0, END)
        entry.insert(0,"player one's turn")
        selection = AiMoves()
        buttons[selection]['text'] = 'O'
        buttonsClicked[selection] = True
        playerOneWon = CheckPlayerWon('X')
        playerTwoWon = CheckPlayerWon('O')
        draw = CheckDraw(buttons)
    

    
    if playerOneWon:
        entry.delete(0, END)
        entry.insert(0, 'player one wins, game over')
    elif playerTwoWon:
        entry.delete(0, END)
        entry.insert(0, 'player two wins, game over')
    elif draw:
        entry.delete(0, END)
        entry.insert(0, 'draw, game over')

def CheckDraw (buttons):
    count = 0
    for index in buttons:
        if index['text'] != '-':
            count += 1
    if count == 9:
        return True
    else:
        return False

def CheckPlayerWon(piece):
    #along the top
    if (button_1['text'] == piece) and (button_2['text'] == piece) and (button_3['text'] == piece):
        button_1['fg'] = 'green'
        button_2['fg'] = 'green'
        button_3['fg'] = 'green'
        return True
    #along the middle
    elif (button_4['text'] == piece) and (button_5['text'] == piece) and (button_6['text'] == piece):
        button_4['fg'] = 'green'
        button_5['fg'] = 'green'
        button_6['fg'] = 'green'
        return True
    #along the bottom
    elif (button_7['text'] == piece) and (button_8['text'] == piece) and (button_9['text'] == piece):
        button_7['fg'] = 'green'
        button_8['fg'] = 'green'
        button_9['fg'] = 'green'
        return True
    #down the left side
    elif (button_1['text'] == piece) and (button_4['text'] == piece) and (button_7['text'] == piece):
        button_1['fg'] = 'green'
        button_4['fg'] = 'green'
        button_7['fg'] = 'green'
        return True
    #down the midddle
    elif (button_2['text'] == piece) and (button_5['text'] == piece) and (button_8['text'] == piece):
        button_2['fg'] = 'green'
        button_5['fg'] = 'green'
        button_8['fg'] = 'green'
        return True
    #down the right side
    elif (button_3['text'] == piece) and (button_6['text'] == piece) and (button_9['text'] == piece):
        button_3['fg'] = 'green'
        button_6['fg'] = 'green'
        button_9['fg'] = 'green'
        return True
    #diagonal top left to bottom right
    elif (button_1['text'] == piece) and (button_5['text'] == piece) and (button_9['text'] == piece):
        button_1['fg'] = 'green'
        button_5['fg'] = 'green'
        button_9['fg'] = 'green'
        return True
    #diagonal top right to bottom left
    elif (button_3['text'] == piece) and (button_5['text'] == piece) and (button_7['text'] == piece):
        button_3['fg'] = 'green'
        button_5['fg'] = 'green'
        button_7['fg'] = 'green'
        return True
    else:
        return False

def AiMoves():
    validOption = False
    #logic for AI to win
    #along the top
    if (button_1['text'] == '-') and (button_2['text'] == 'O') and (button_3['text'] == 'O'):
        return 0 
    elif (button_1['text'] == 'O') and (button_2['text'] == '-') and (button_3['text'] == 'O'):
        return 1
    elif (button_1['text'] == 'O') and (button_2['text'] == 'O') and (button_3['text'] == '-'):
        return 2
    else:
        pass
    #along the middle
    if (button_4['text'] == '-') and (button_5['text'] == 'O') and (button_6['text'] == 'O'):
        return 3
    elif (button_4['text'] == 'O') and (button_5['text'] == '-') and (button_6['text'] == 'O'):
        return 4
    elif (button_4['text'] == 'O') and (button_5['text'] == 'O') and (button_6['text'] == '-'):
        return 5
    else:
        pass
    #along the bottom
    if (button_7['text'] == '-') and (button_8['text'] == 'O') and (button_9['text'] == 'O'):
        return 6
    elif (button_7['text'] == 'O') and (button_8['text'] == '-') and (button_9['text'] == 'O'):
        return 7
    elif (button_7['text'] == 'O') and (button_8['text'] == 'O') and (button_9['text'] == '-'):
        return 8
    else:
        pass
    #down the left side
    if (button_1['text'] == '-') and (button_4['text'] == 'O') and (button_7['text'] == 'O'):
        return 0
    elif (button_1['text'] == 'O') and (button_4['text'] == '-') and (button_7['text'] == 'O'):
        return 3
    elif (button_1['text'] == 'O') and (button_4['text'] == 'O') and (button_7['text'] == '-'):
        return 6
    else:
        pass
    #down the middle
    if (button_2['text'] == '-') and (button_5['text'] == 'O') and (button_8['text'] == 'O'):
        return 1
    elif (button_2['text'] == 'O') and (button_5['text'] == '-') and (button_8['text'] == 'O'):
        return 4
    elif (button_2['text'] == 'O') and (button_5['text'] == 'O') and (button_8['text'] == '-'):
        return 7
    else:
        pass
    #down the right
    if (button_3['text'] == '-') and (button_6['text'] == 'O') and (button_9['text'] == 'O'):
        return 2
    elif (button_3['text'] == 'O') and (button_6['text'] == '-') and (button_9['text'] == 'O'):
        return 5
    elif (button_3['text'] == 'O') and (button_6['text'] == 'O') and (button_9['text'] == '-'):
        return 8
    else:
        pass
    #diagonal top left to bottom right
    if (button_1['text'] == '-') and (button_5['text'] == 'O') and (button_9['text'] == 'O'):
        return 0
    elif (button_1['text'] == 'O') and (button_5['text'] == '-') and (button_9['text'] == 'O'):
        return 4
    elif (button_1['text'] == 'O') and (button_5['text'] == 'O') and (button_9['text'] == '-'):
        return 8
    else:
        pass
    #diagonal top right to bottom left
    if (button_3['text'] == '-') and (button_5['text'] == 'O') and (button_7['text'] == 'O'):
        return 2
    elif (button_3['text'] == 'O') and (button_5['text'] == '-') and (button_7['text'] == 'O'):
        return 4
    elif (button_3['text'] == 'O') and (button_5['text'] == 'O') and (button_7['text'] == '-'):
        return 6
    else:
        pass

    #logic for blocking the player from winning
    #along the top
    if (button_1['text'] == '-') and (button_2['text'] == 'X') and (button_3['text'] == 'X'):
        return 0 
    elif (button_1['text'] == 'X') and (button_2['text'] == '-') and (button_3['text'] == 'X'):
        return 1
    elif (button_1['text'] == 'X') and (button_2['text'] == 'X') and (button_3['text'] == '-'):
        return 2
    else:
        pass
    #along the middle
    if (button_4['text'] == '-') and (button_5['text'] == 'X') and (button_6['text'] == 'X'):
        return 3
    elif (button_4['text'] == 'X') and (button_5['text'] == '-') and (button_6['text'] == 'X'):
        return 4
    elif (button_4['text'] == 'X') and (button_5['text'] == 'X') and (button_6['text'] == '-'):
        return 5
    else:
        pass
    #along the bottom
    if (button_7['text'] == '-') and (button_8['text'] == 'X') and (button_9['text'] == 'X'):
        return 6
    elif (button_7['text'] == 'X') and (button_8['text'] == '-') and (button_9['text'] == 'X'):
        return 7
    elif (button_7['text'] == 'X') and (button_8['text'] == 'X') and (button_9['text'] == '-'):
        return 8
    else:
        pass
    #down the left side
    if (button_1['text'] == '-') and (button_4['text'] == 'X') and (button_7['text'] == 'X'):
        return 0
    elif (button_1['text'] == 'X') and (button_4['text'] == '-') and (button_7['text'] == 'X'):
        return 3
    elif (button_1['text'] == 'X') and (button_4['text'] == 'X') and (button_7['text'] == '-'):
        return 6
    else:
        pass
    #down the middle
    if (button_2['text'] == '-') and (button_5['text'] == 'X') and (button_8['text'] == 'X'):
        return 1
    elif (button_2['text'] == 'X') and (button_5['text'] == '-') and (button_8['text'] == 'X'):
        return 4
    elif (button_2['text'] == 'X') and (button_5['text'] == 'X') and (button_8['text'] == '-'):
        return 7
    else:
        pass
    #down the right
    if (button_3['text'] == '-') and (button_6['text'] == 'X') and (button_9['text'] == 'X'):
        return 2
    elif (button_3['text'] == 'X') and (button_6['text'] == '-') and (button_9['text'] == 'X'):
        return 5
    elif (button_3['text'] == 'X') and (button_6['text'] == 'X') and (button_9['text'] == '-'):
        return 8
    else:
        pass
    #diagonal top left to bottom right
    if (button_1['text'] == '-') and (button_5['text'] == 'X') and (button_9['text'] == 'X'):
        return 0
    elif (button_1['text'] == 'X') and (button_5['text'] == '-') and (button_9['text'] == 'X'):
        return 4
    elif (button_1['text'] == 'X') and (button_5['text'] == 'X') and (button_9['text'] == '-'):
        return 8
    else:
        pass
    #diagonal top right to bottom left
    if (button_3['text'] == '-') and (button_5['text'] == 'X') and (button_7['text'] == 'X'):
        return 2
    elif (button_3['text'] == 'X') and (button_5['text'] == '-') and (button_7['text'] == 'X'):
        return 4
    elif (button_3['text'] == 'X') and (button_5['text'] == 'X') and (button_7['text'] == '-'):
        return 6
    else:
        pass
    
    selection = random.randint(0,8)
    while not validOption:
        if (buttonsClicked[selection]):
            selection = random.randint(0,8)
        else:
            return selection
        
root = Tk()
root.title('Welcome to my TicTacToe Game')

entry = Entry(root, width=60, borderwidth=5)

button_1 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: Button_Click(0))
button_2 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: Button_Click(1))
button_3 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: Button_Click(2))
button_4 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: Button_Click(3))
button_5 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: Button_Click(4))
button_6 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: Button_Click(5))
button_7 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: Button_Click(6))
button_8 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: Button_Click(7))
button_9 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: Button_Click(8))
button_clear = Button(root, text='clear', fg = 'black', padx=190, pady=15, command=lambda: Reset(buttons))

buttons = [button_1 ,button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]

entry.insert(0,"player one's turn")

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

entry.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

button_clear.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

button1Clicked = False
button2Clicked = False
button3Clicked = False
button4Clicked = False
button5Clicked = False
button6Clicked = False
button7Clicked = False
button8Clicked = False
button9Clicked = False

buttonsClicked = [button1Clicked, button2Clicked, button3Clicked, button4Clicked, button5Clicked, button6Clicked, button7Clicked, button8Clicked, button9Clicked]

root.mainloop()