

def printStuff(thing):
	global oldprint
	oldprint("Stuff and " + str(thing))

oldprint = print
a = 5
print = printStuff

print(a)
print("Nothing")