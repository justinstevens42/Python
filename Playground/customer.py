#Description:  Prints information about a customer
#Functions:  Withdraw money, Deposit money, Print Customer Information
#Original:  https://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/
#Modified by Justin Stevens  
class Customer(object):

	def __init__(self, name, balance):
		self.name=name
		self.balance=balance
	def withdraw(self, amount):
		if amount>self.balance:
			raise RuntimeError('Amount greater than available')
		self.balance-=amount
		return self.balance
	def deposit(self, amount):
		self.balance+=amount
		return self.balance
	def printcustomer(self):
		print "Name: ", self.name 
		print "Balance: ", self.balance
		print "\n"
def main():
	Person=Customer("Name", 7000)
	Person.printcustomer()
	Person.name="Person"
	Person.withdraw(800)
	Person.printcustomer()
main()


