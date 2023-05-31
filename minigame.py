from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from multiprocessing.dummy import Value
from turtle import title
import random
from random import randint


mainpage=Tk()
mainpage.title('Menu')
mainpage.geometry('900x600')
mainpage.config(bg='#EAF6F6')

# setting (unfinished)
setting = Button(mainpage, text='*', font=('Arial Rounded MT Bold', 40), fg='#FFCC8F', bg='#EAF6F6', activebackground='#EAF6F6', relief='flat', width=3, height=1)
setting.pack(anchor=E, ipadx=0, ipady=0)

#Mini games
name = Label(text='Mini Games', fg='#66BFBF', bg='#EAF6F6', font=('Arial Rounded MT Bold', 55, 'bold'))
name.pack(anchor=CENTER)

# rock peper scissors game button
rps = Button(mainpage, text='Rock Paper Scissors', font=('Arial Rounded MT Bold', 20), fg='#66BFBF', bg='#FFFFFF', activebackground='#66BFBF', relief='ridge', borderwidth=1, command=lambda:rockpaperscissors())
rps.pack(anchor=CENTER, pady=40, ipadx=15, ipady=5)

# tic tac toe game button
ttt = Button(mainpage, text='Tic Tac Toe', font=('Arial Rounded MT Bold', 20), fg='#66BFBF', bg='#FFFFFF', activebackground='#66BFBF', relief='ridge', borderwidth=1, command=lambda:tictactoe())
ttt.pack(anchor=CENTER, ipadx=15, ipady=5)

# exit game button
e = Button(mainpage, text='Quit', font=('Arial Rounded MT Bold', 20), fg='#FFFFFF', bg='#F56A79', activebackground='#FF8B8B', relief='ridge', borderwidth=1, command=lambda:mainpage.destroy())
e.pack(anchor=CENTER, pady=40, ipadx=6, ipady=2)


def rockpaperscissors():
    rgpage=Toplevel(mainpage)
    rgpage.title('Rock Paper Scissors')
    rgpage.geometry('900x660')
    rgpage.config(bg='#EAF6F6')

    mainpage.withdraw()
    rname = Label(rgpage, text='Rock Paper Scissors!', font=('Arial Rounded MT Bold', 40, 'bold'), fg='#66BFBF', bg='#EAF6F6')
    rname.grid(row=0, column=0, columnspan=8, padx=150, pady=30)

    bot = Label(rgpage, text='BOT', font=('Arial Rounded MT Bold', 24, 'bold'), fg='#FF0063', bg='#EAF6F6')
    bot.grid(row=1, column=0, padx=100)

    user = Label(rgpage, text='YOU', font=('Arial Rounded MT Bold', 24, 'bold'), fg='#3AB0FF', bg='#EAF6F6')
    user.grid(row=1, column=2,)

    x=IntVar(value=' ')

    rock = PhotoImage(file='Rc2.png')
    paper = PhotoImage(file='Pa2.png')
    scissors =  PhotoImage(file='Sc2.png')

    rockme = PhotoImage(file='Rc1.png')
    paperme = PhotoImage(file='Pa1.png')
    scissorsme =  PhotoImage(file='Sc1.png')

    #add image to a list
    image_list = [rock,paper,scissors]

    #pick random number 0-2:''
    pick_number = randint(0,2)

    #throw up an image when the program starts
    image_label = Label(rgpage, image = image_list[pick_number], bd=0, bg='#EAF6F6')
    image_label.grid(row=2, column=0, padx=90)

    #make our choice
    rad1 = Radiobutton(rgpage, text='rock', font=('Arial Rounded MT Bold', 26), fg='#3AB0FF', bg='#EAF6F6', variable=x, value=0)
    rad1.grid(row=4, column=0, padx=10, pady=10)
    rad2 = Radiobutton(rgpage, text='paper', font=('Arial Rounded MT Bold', 26), fg='#3AB0FF', bg='#EAF6F6', variable=x, value=1)
    rad2.grid(row=4, column=1, padx=10, pady=10)
    rad3 = Radiobutton(rgpage, text='scissors', font=('Arial Rounded MT Bold', 26), fg='#3AB0FF', bg='#EAF6F6', variable=x, value=2)
    rad3.grid(row=4, column=2, padx=100, pady=10)
    
    #create spin function
    def spin():
        value = x.get()
        # pick random number
        pick_number = randint(0,2)
  
        # show image
        image_label.config(image=image_list[pick_number], bg='#EAF6F6')
        # 0 = rock , 1 = paper , 2 = scissors
    
        # convert dropdown choice
        if value  == 0:
            user_choice_value = 0
            mage_label2 = Label(rgpage, image = rockme, bg='#EAF6F6')
            mage_label2.grid(row=2, column=2, padx=100)
        elif value  == 1:
            user_choice_value = 1
            mage_label3 = Label(rgpage, image = paperme, bg='#EAF6F6')
            mage_label3.grid(row=2, column=2, padx=100)
        elif value  == 2:
            user_choice_value = 2
            mage_label4 = Label(rgpage, image = scissorsme, bg='#EAF6F6')
            mage_label4.grid(row=2, column=2, padx=100)

        b = 0    
        u = 0
        #determine if we won or lost
        if user_choice_value == 0: #rock
            if pick_number == 0:
                win_lose_label.config(text='Draw!!', fg='#A267AC', bg='#EAF6F6')
            elif pick_number == 1:
                win_lose_label.config(text='You lose...', fg='#A267AC', bg='#EAF6F6')
                b += 1
                bs = int(score_bot.get())
                score_bot.delete(0, END)
                score_bot.insert(END, f'{bs + b}')
            elif pick_number == 2:
                win_lose_label.config(text='You win!', fg='#A267AC', bg='#EAF6F6')
                u += 1
                us = int(score_user.get())
                score_user.delete(0, END)
                score_user.insert(END, f'{us + u}')
                
        if user_choice_value == 1: #paper
            if pick_number == 0:
                win_lose_label.config(text='You win!', fg='#A267AC', bg='#EAF6F6')
                u += 1
                us = int(score_user.get())
                score_user.delete(0, END)
                score_user.insert(END, f'{us + u}')
            elif pick_number == 1:
                win_lose_label.config(text='Draw!!', fg='#A267AC', bg='#EAF6F6')
            elif pick_number == 2:
                win_lose_label.config(text='You lose...', fg='#A267AC', bg='#EAF6F6')
                b += 1
                bs = int(score_bot.get())
                score_bot.delete(0, END)
                score_bot.insert(END, f'{bs + b}')

        if user_choice_value == 2: #scissors
            if pick_number == 0:
                win_lose_label.config(text='You lose...', fg='#A267AC', bg='#EAF6F6')
                b += 1
                bs = int(score_bot.get())
                score_bot.delete(0, END)
                score_bot.insert(END, f'{bs + b}')
            elif pick_number == 1:
                win_lose_label.config(text='You win!', fg='#A267AC', bg='#EAF6F6')
                u += 1
                us = int(score_user.get())
                score_user.delete(0, END)
                score_user.insert(END, f'{us + u}')
            elif pick_number == 2:
                win_lose_label.config(text='Draw!!', fg='#A267AC', bg='#EAF6F6')

        usg =  int(score_user.get())
        bsg =  int(score_bot.get())      
        if usg == 3:
            score_user.delete(0, END)
            score_bot.delete(0, END)
            score_user.insert(END, 0)
            score_bot.insert(END, 0)
            h = open('Yourstatistic.txt','w')
            h.write(f'You lose\tScores| {bsg} : {usg}\n')
            h.close()
            r = open('Yourstatistic.txt','r')
            messagebox.showinfo('Your records', r.readline())
            r.close()
        elif bsg == 3:
            score_user.delete(0, END)
            score_bot.delete(0, END)
            score_user.insert(END, 0)
            score_bot.insert(END, 0)
            h = open('Yourstatistic.txt','w')
            h.write(f'You lose\tScores| {bsg} : {usg}')
            h.close()
            r = open('Yourstatistic.txt','r')
            messagebox.showinfo('Your records', r.readline())
            r.close()

    #create spin button 
    spin_button = Button(rgpage, text='spin', font=('Arial Rounded MT Bold', 18), fg='#FFFFFF', bg='#FFCC8F',command=lambda:spin())
    spin_button.grid(row=5, column=1, padx=20, pady=35)
    
    #label for showing if you won or not
    win_lose_label = Label(rgpage, text='Results', font=('Arial Rounded MT Bold', 30), fg='#EAF6F6', bg='#A267AC', relief='flat')
    win_lose_label.grid(row=2, column=1)
    

    score_user = Entry(rgpage, font=('Arial Rounded MT Bold', 24), fg='#3AB0FF', bg='#FFFFFF', width=1)
    score_user.grid(row=3, column=2, pady=15)
    score_user.insert(END, 0)

    score_bot = Entry(rgpage, font=('Arial Rounded MT Bold', 24), fg='#FF0063', bg='#FFFFFF', width=1)
    score_bot.grid(row=3, column=0, pady=15)
    score_bot.insert(END, 0)

    # back to menu    
    btm = Button(rgpage, text='Menu', font=('Arial Rounded MT Bold', 14), fg='#FFFFFF', bg='#66BFBF', activebackground='#FFE7BF', relief='ridge', borderwidth=1, command=lambda:[mainpage.deiconify(), rgpage.destroy()])
    btm.grid(row=6, column=0)

    # exit game
    e = Button(rgpage, text='Quit', font=('Arial Rounded MT Bold', 14), fg='#FFFFFF', bg='#F56A79', activebackground='#FF8B8B', relief='ridge', borderwidth=1, command=lambda:[mainpage.destroy()])
    e.grid(row=6, column=2)

mainpage.mainloop()  