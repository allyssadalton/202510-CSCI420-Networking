from tkinter import *
import time

master = Tk()

master.geometry("800x100")
master.configure(background="black")
colors = ['black', 'green', 'blue','purple','white']
a = 1

def changeColor(event=None):
	global master
	global colors
	global a
	print(dir(event))
	print(event.x)
	print(event.y)
	master.configure(background=colors[a])
	a += 1
	a = a % len(colors)
	#master.after(500, changeColor)

def textentered(event=None):
	global box
	print(box.get("1.0", "end-1c"))

b1 = Button(master, text="Click me")
b1.grid(column=1, row=1)
b1.bind('<Button>', changeColor)

b2 = Button(master, text="Click me")
b2.grid(column=2, row=2)
b2.bind('<Button>', changeColor)

box = Text(master, height=1, width=20)
box.grid(column=2, row=1)
box.bind('<Return>', textentered)

l = Label(master, text="This is a label")
l.grid(column=3, row=1)

master.bind('<Button-1>', changeColor)

mainloop()