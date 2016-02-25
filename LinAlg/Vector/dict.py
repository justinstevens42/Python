class Vec:
	def __init__(self, labels, function):
		self.D=labels
		self.f=function  
	def setitem(self, d,val):
		if d in self.D:
			pass
		else:
			self.D.append(d)
		self.f[d]=val
	def getitem(self, d):
		if d in self.f:
			return self.f[d]
		else:
			return 0
	def zero_vec(self):
		for d in self.D:
			self.f[d]=0
def list2vec(L):
	v=Vec(range(len(L)), {})
	for i in range(len(L)):
		v.f[i]=L[i]
	return v
x=Vec([],{})
x.setitem('A',1)
print x.getitem('A')
print x.D