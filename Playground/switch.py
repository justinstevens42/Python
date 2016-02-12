#Description:  A neat way to implement switch statements in Python
#Author:  Justin Stevens, modified from http://www.voidspace.org.uk/python/articles/OOP.shtml

def Function1():
	print "You chose one "
def Function2():
	print "You chose two "
def Function3():
	print "You chose three "
def main():
	switch={'1': Function1, '2': Function2, '3': Function3}
	flag=1
	while(flag):
		choice=raw_input("Enter an integer from 1 to 3, inclusive: ")
		try:
			result=switch[choice]
		except KeyError:
			print("Your choice is not valid ")
		else:
			flag=0 #exit the while loop
			result() #print the result of the Function
main()

