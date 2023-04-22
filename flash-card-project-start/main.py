import random
from tkinter import *
import pandas
import os
BACKGROUND_COLOR = "#B1DDC6"
window=Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("flashy")
right_mark=PhotoImage(file="images/right.png")
wrong_mark=PhotoImage(file="images/wrong.png")
try:
    word = pandas.read_csv("data/words_to_learn.csv")


except:
    word=pandas.read_csv("data/french_words.csv")


dictionary=word.to_dict(orient="records")
print(dictionary)
ran={}
def functionr():
    global ran
    ran=random.choice(dictionary)
    def english():

        canvas.itemconfig(card_image, image=card_rear)
        canvas.itemconfig(title, text="English",fill="white")
        canvas.itemconfig(Word, text=ran["English"],fill="white")

    def change_text():
        canvas.itemconfig(card_image,image=card_front)
        canvas.itemconfig(title,text="French",fill="black")
        canvas.itemconfig(Word,text=ran["French"],fill="black")
        window.after(3000,english)
    change_text()
def functionw():
    global ran
    if(os.path.isfile("data/words_to_learn.csv")):
        with open("data/words_to_learn.csv","a") as file:
            file.write(ran["French"]+","+ran["English"]+"\n")
    else:
        with open("data/words_to_learn.csv","a") as file:
            file.write("French,English\n")
    ran=random.choice(dictionary)
    def english():

        canvas.itemconfig(card_image, image=card_rear)
        canvas.itemconfig(title, text="English",fill="white")
        canvas.itemconfig(Word, text=ran["English"],fill="white")

    def change_text():
        canvas.itemconfig(card_image,image=card_front)
        canvas.itemconfig(title,text="French",fill="black")
        canvas.itemconfig(Word,text=ran["French"],fill="black")
        window.after(3000,english)
    change_text()



right_button=Button(image=right_mark,highlightthickness=0,command=functionr)
right_button.grid(row=1,column=2)
wrong_button=Button(image=wrong_mark,highlightthickness=0,command=functionw)
wrong_button.grid(column=0,row=1)
card_front=PhotoImage(file="images/card_front.png")
card_rear=PhotoImage(file="images/card_back.png")
canvas=Canvas(height=550,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_image=canvas.create_image(400,275,image=card_front)
title=canvas.create_text(400,150,text="Title",fill="black",font=("Arial",40,"italic"))
Word=canvas.create_text(400,263,text="Word",fill="black",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=3)
functionr()

window.mainloop()
