from tkinter import *
import time
import threading

master = Tk()

master.geometry("800x800")
master.configure(background="black")
colors = ['black', 'green', 'blue','purple','white']
a = 1
run = True

def changeColor(event=None):
	global master
	global colors
	global a
	global run
	while run:
		master.configure(background=colors[a])
		a += 1
		a = a % len(colors)
		time.sleep(1)
	

#master.after(500, changeColor)
t1 = threading.Thread(target = changeColor)
t1.start()

mainloop()
print("Past mainloop")
run = False