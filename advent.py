f=open('data', 'r')
data=f.readlines()[0]
data=str(data)
print len(data)
counter=0
for i in range(0, len(data)):
	if data[i]=='(':
		counter+=1
	if data[i]==')':
		counter-=1
	if counter<0:
		break
print i
