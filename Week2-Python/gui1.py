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
	master.configure(background=colors[a])
	a += 1
	a = a % len(colors)
	master.after(500, changeColor)

master.after(500, changeColor)

mainloop()