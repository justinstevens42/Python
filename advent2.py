g=open('data2', 'r')
data=g.readlines()[0].strip('\n')
for i in range(1000):
	d={}
	print i
	d[i]=g.readlines()[i].strip('\n')
print d[2]