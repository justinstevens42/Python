import math
def base(n,b):
	base_rep=""
	if b>0:
		while(n!=0):
			rem=str(n%b)
			base_rep=rem+base_rep
			n=n/b
	if b<0:
		#only difference is you take the ceiling when the base is negative
		while(n!=0):
			rem=str(n%-b)
			base_rep=rem+base_rep
			n=int(math.ceil(float(n)/b))
	return base_rep
def baseimaginary(n):
	""" Base -1+i representation of n.  Base -4 is used as an intermediary step"""
	if n==0:
		return 0
	neg4base_rep=base(n,-4)
	imagbase_rep=""
	for i in neg4base_rep:
		if i=="0":
			imagbase_rep=imagbase_rep+"0000"
		if i=="1":
			imagbase_rep=imagbase_rep+"0001"
		if i=="2":
			imagbase_rep=imagbase_rep+"1100"
		if i=="3":
			imagbase_rep=imagbase_rep+"1101"
	return imagbase_rep.lstrip("0")
def main():
	"""Returns the base -1+i representation for all integers from -x to x"""
	print "This program will return the base -1+i representation for integers from -x to x"
	x=int(raw_input("What would you like x to be? "))
	for i in range(-x,x+1):
		print "The base -1+i representation of", i , "is", baseimaginary(i)
main()			

