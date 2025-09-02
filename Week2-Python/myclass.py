# CSCI 420 Python Demo
# Paul Talaga
# Sept 2, 2025

class Bank:
	def __init__(self, name = "None given"):
		self.customers = [] # Note the list to store customers
		self.name = name

	def printCustomers(self):
		print(f"There are {len(self.customers)} in bank {self.name}")
		for c in self.customers:
			print(c)

	def addCustomer(self, customer):
		self.customers.append( [customer,0] )

	def addMoney(self, customer, amt):
		for c in self.customers:
			if c[0] == customer:
				c[1] += amt 
				return True
		print(f"{customer} is not a customer in this bank")
		return False







boa = Bank("Bank of America")
boa.addCustomer("Rainey")
boa.addMoney("Rainey", 20.25)
boa.addMoney("Rainey", 1.25)

bmo = Bank("Bank of Montreal")

chase = Bank("Chase Bank")

boa.printCustomers()
bmo.printCustomers()
chase.printCustomers()