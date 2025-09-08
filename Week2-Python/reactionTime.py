from tkinter import *
import time
import random

master = Tk()

master.geometry("800x100")
master.configure(background="blue")
#colors = ['black', 'green', 'blue','purple','white']
startTime = -1

def changeColor(event=None):
	global master
	global startTime
	startTime = time.time()  # seconds
	master.configure(background="Red")

	

def clicked(event=None):
	global startTime
	if startTime == -1:
		print("Clicked before change!!!!!")
	else:
		elapsed = time.time() - startTime
		print(f"Reaction Time (s) {elapsed}")
		startTime = -1
		time.sleep(0.5)
		master.configure(background="blue")
		master.after(random.randint(1000, 5000), changeColor)
	



l = Label(master, text="Click the screen when the color changes to red!")
l.grid(column=1, row=1)

master.bind('<Button-1>', clicked)

master.after(random.randint(1000, 5000), changeColor)

mainloop()