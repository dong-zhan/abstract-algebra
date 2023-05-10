# import zd
# import math_zd.perm as perm
#
# import importlib
# importlib.reload(perm)

import math

def rrr():
	importlib.reload(perm)
	
def imp():
	global math
	import math as math
	
def perm(X):
 
	if len(X) == 0:
		return []
 
	if len(X) == 1:
		return [X]

	P = [] 
 
	for i in range(len(X)):
	   x = X[i]
 
	   for p in perm(X[:i] + X[i+1:]):
		   P.append([x] + p)
		   
	return P



