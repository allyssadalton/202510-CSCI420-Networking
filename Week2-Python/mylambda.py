
thing = lambda b: b + 1

def thing2(b):
	return b + 1

a = map(thing2, range(10))
print(list(a))

print(thing(5))