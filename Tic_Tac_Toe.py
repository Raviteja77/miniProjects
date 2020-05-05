import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("1450x900+0+0")
root.title("Tic Tac Toe")
root.configure(background = "sky blue")

Tops = Frame(root, bg = 'sky blue', pady = 2, width = 1350, height = 100, relief = RIDGE)
Tops.grid(row = 0, column = 0)

labelTitle = Label(Tops, font = ('Courier' , 50, 'bold'),
                   text = "Tic Tac Toe", bd = 20, bg = 'Cadet blue', fg = 'cornsilk', justify = CENTER)
labelTitle.grid(row = 0, column = 0)

MainFrame = Frame(root, bg = 'powder blue', pady = 2, width = 1350, height = 600, relief = RIDGE)
MainFrame.grid(row = 1, column = 0)

leftFrame = Frame(MainFrame, bd = 10, width = 750, height = 500, pady = 3, padx = 10,
                  bg = 'Cadet blue', relief = RIDGE)
leftFrame.pack(side = LEFT)

rightFrame = Frame(MainFrame, bd = 10, width = 560, height = 500, pady = 3, padx = 10,
                  bg = 'Cadet blue', relief = RIDGE)
rightFrame.pack(side = RIGHT)

rightFrame0 = Frame(rightFrame, bd = 10, width = 560, height = 150, padx = 10, pady = 2,
                    bg = 'Cadet blue', relief = RIDGE)
rightFrame0.grid(row = 0, column = 0)

rightFrame1 = Frame(rightFrame, bd = 10, width = 560, height = 150, pady = 2, padx = 10,
                  bg = 'Cadet blue', relief = RIDGE)
rightFrame1.grid(row = 1, column = 0)

PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

p1 = StringVar()
p2 = StringVar()

bclick = True
flag = 0

def button_click(buttons):
    global bclick, flag, player1_name, player2_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        check_for_win()
        flag += 1

    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        check_for_win()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def check_for_win():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
       button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
       button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
       button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
       button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
       button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
       button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
       button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
       button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
       tkinter.messagebox.showinfo("Tic Tac Toe" , pa)
    elif flag == 8:
        tkinter.messagebox.showinfo("Tic Tac Toe","Its a Tie")
    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
       button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
       button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
       button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
       button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
       button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
       button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
       button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
       button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
       tkinter.messagebox.showinfo("Tic Tac Toe" , playerb)


def reset():
    global flag
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
    flag = 0


def Newgame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)

buttons = StringVar()

labelTitle = Label(rightFrame0, font = ('Courier' , 26, 'bold'),
                   text = "Player1: ", bd = 20, bg = 'Cadet blue')
labelTitle.grid(row = 0, column = 0, sticky = W)
txtPlayerX_name = Entry(rightFrame0, font = ('Courier' , 26, 'bold'),bd = 2, fg = 'black',
                   textvariable = p1, width = 14, justify = LEFT).grid(row = 0, column = 1)

labelTitle = Label(rightFrame0, font = ('Courier' , 26, 'bold'),
                   text = "Player2: ", bd = 20, bg = 'Cadet blue')
labelTitle.grid(row = 1,  column = 0, sticky = W)
txtPlayerO_name = Entry(rightFrame0, font = ('Courier' , 26, 'bold'),bd = 2, fg = 'black',
                   textvariable = p2, width = 14, justify = LEFT).grid(row = 1, column = 1)


buttonreset = Button(rightFrame1, text = "Reset", font = ('Courier' , 26, 'bold'), height = 2, width = 12,
                     bg = 'red', fg = 'gainsboro', command = reset)
buttonreset.grid(row = 0, column = 0)

buttonNewgame = Button(rightFrame1, text = "New Game", font = ('Courier' , 26, 'bold'), height = 2, width = 12,
                     bg = 'green', fg = 'gainsboro', command = Newgame)
buttonNewgame.grid(row = 0, column = 1)



button1 = Button(leftFrame, text = " ", font = "Times 26 bold", height = 3, width = 8, bg = 'gainsboro', command = lambda: button_click(button1))
button1.grid(row = 1, column = 0, sticky = S+N+W+E)

button2 = Button(leftFrame, text = " ", font = "Times 26 bold", height = 3, width = 8, bg = 'gainsboro', command = lambda: button_click(button2))
button2.grid(row = 1, column = 1, sticky = S+N+W+E)

button3 = Button(leftFrame, text = " ", font = "Times 26 bold", height = 3, width = 8, bg = 'gainsboro', command = lambda: button_click(button3))
button3.grid(row = 1, column = 2, sticky = S+N+W+E)

button4 = Button(leftFrame, text = " ", font = "Times 26 bold", height = 3, width = 8, bg = 'gainsboro', command = lambda: button_click(button4))
button4.grid(row = 2, column = 0, sticky = S+N+W+E)

button5 = Button(leftFrame, text = " ", font = "Times 26 bold", height = 3, width = 8, bg = 'gainsboro', command = lambda: button_click(button5))
button5.grid(row = 2, column = 1, sticky = S+N+W+E)

button6 = Button(leftFrame, text = " ", font = "Times 26 bold", height = 3, width = 8, bg = 'gainsboro', command = lambda: button_click(button6))
button6.grid(row = 2, column = 2, sticky = S+N+W+E)

button7 = Button(leftFrame, text = " ", font = "Times 26 bold", height = 3, width = 8, bg = 'gainsboro', command = lambda: button_click(button7))
button7.grid(row = 3, column = 0, sticky = S+N+W+E)

button8 = Button(leftFrame, text = " ", font = "Times 26 bold", height = 3, width = 8, bg = 'gainsboro', command = lambda: button_click(button8))
button8.grid(row = 3, column = 1, sticky = S+N+W+E)

button9 = Button(leftFrame, text = " ", font = "Times 26 bold", height = 3, width = 8, bg = 'gainsboro', command = lambda: button_click(button9))
button9.grid(row = 3, column = 2, sticky = S+N+W+E)

root.mainloop()