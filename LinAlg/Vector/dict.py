class Vec:
	def __init__(self, labels, function):
		self.D=labels
		self.f=function  

def zero_vec(D):
	return Vec(D, {d:0 for d in D})
x=zero_vec(('A', 'B', 'C'))
print x.D
print x.f