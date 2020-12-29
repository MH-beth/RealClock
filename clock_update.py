import sys
from tkinter import *
import time
import datetime



def tick():
    global time_string
    time_string = time.strftime("%H:%M")
    time_string = str(time_string)
    second_string = time.strftime("%S")
    clock.config(text = time_string)
    clock_seconds.config(text = second_string)
    clock_seconds.after(200 , tick)

def date_getter():
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    date = f"{day}/{month}/{year}"
    date_hello.config(text = date)
    date_hello.after(200 , date_getter)

def quit_screen3():
    screen3.destroy()

def hello():
    global clock
    global screen3
    global clock_seconds
    global date_hello
    screen3 = Toplevel(screen2)
    screen3.title("hello   body")
    Label(screen3,text = "").pack()
    date_hello = Label(screen3, font=("Calibri", 150))
    date_hello.pack()
    clock = Label(screen3,font=("Calibri", 100))
    clock.pack()
    clock_seconds = Label(screen3, font=("Calibri", 100))
    clock_seconds.pack()
    tick()
    date_getter()
    Button(screen3 , text = "quit",font = ("Calibni", 50),command = quit_screen3).pack()
screen2 = Tk()
screen2.title("time budy")
Button(screen2,text = "get time now", command = hello).pack()
screen2.mainloop()
