
import tkinter as tk
root = tk.Tk()
canvas= tk.Canvas (
                        master = root,
                        bg = "white",
                        highlightthickness=0
                    )

canvas.grid(row = 1, column = 1,sticky="nsew", columnspan =1, rowspan=1)
canvas.create_text(30,30, text = 'hello 1', fill = 'black', font = 'Arial 12' )


def test1(canvas):
    canvas.create_text(40,40, text = 'hello 1', fill = 'black', font = 'Arial 12' )
    root.after(1000, test2(canvas))


def test2(canvas):
    canvas.create_text(50,50, text = 'hello 1', fill = 'orange', font = 'Arial 12' )
    root.after(1000, test1(canvas))

root.mainloop()

test1(canvas) 
# from tkinter import *
# import datetime

# root = Tk()

# lab = Label(root)
# lab.pack()

# def clock():
#     time = datetime.datetime.now().strftime("Time: %H:%M:%S")
#     lab.config(text=time)
#     #lab['text'] = time
#     root.after(1000, clock) # run itself again after 1000 ms
    
# # run first time
# clock()

# root.mainloop()