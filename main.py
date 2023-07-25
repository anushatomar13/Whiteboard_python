from tkinter import *
from tkinter.colorchooser import askcolor
import tkinter as tk
from turtle import color as turtle_color

root = Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False, False)

current_x = 0
current_y = 0
color = "black"

def locate_xy(event):
    global current_x, current_y
    current_x = event.x
    current_y = event.y

def add_line(event):
    global current_x, current_y
    canvas.create_line(current_x, current_y, event.x, event.y, width=get_current_value(), fill=color, capstyle=ROUND, smooth=True)
    current_x, current_y = event.x, event.y

def show_color(new_color):
    global color
    color = new_color

def new_canvas():
    canvas.delete('all')
    display_palette()

def display_palette():
    colors.create_rectangle(10, 10, 30, 30, fill='black')
    colors.create_rectangle(10, 40, 30, 60, fill='grey')
    colors.create_rectangle(10, 70, 30, 90, fill='brown4')
    colors.create_rectangle(10, 100, 30, 120, fill='red')
    colors.create_rectangle(10, 130, 30, 150, fill='orange')
    colors.create_rectangle(10, 160, 30, 180, fill='yellow')
    colors.create_rectangle(10, 190, 30, 210, fill='green')
    colors.create_rectangle(10, 220, 30, 240, fill='blue')
    colors.create_rectangle(10, 250, 30, 270, fill='purple')

    colors.tag_bind(ALL, '<Button-1>', lambda event: show_color(colors.itemcget(CURRENT, 'fill')))

colors = Canvas(root, bg="#ffffff", width=37, height=300, bd=0)
colors.place(x=30, y=60)
display_palette()

canvas = Canvas(root, width=930, height=500, background="#fff", cursor="hand2")
canvas.place(x=100, y=10)

canvas.bind('<Button-1>', locate_xy)
canvas.bind('<B1-Motion>', add_line)

##### Slider ######

current_value = tk.DoubleVar()

def get_current_value():
    return '{:.2f}'.format(current_value.get())

def slider_changed(event):
    value_label.configure(text=get_current_value())

slider = tk.Scale(root, from_=0, to=100, orient='horizontal', command=slider_changed, variable=current_value)
slider.place(x=30, y=530)

# Value label
value_label = tk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

root.mainloop()
