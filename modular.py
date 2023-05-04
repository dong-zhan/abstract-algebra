# import zd
# import math_zd.modular as modular
#
# import importlib
# importlib.reload(modular)

from math import gcd
import util.arr as arr
import math
import random

def imp():
	global gcd, math
	from math import gcd
	import math
	
# copy rrr() to IDLE, run from there.
# import importlib
def rrr():
	importlib.reload(modular)
	
# https://en.wikipedia.org/wiki/Modular_exponentiation
def modular_pow1(b, e, m):
	"""
	This algorithm makes use of the identity
	(a·b) mod m = [(a mod m)·(b mod m)] mod m
	b: base, e: exp, m: modulus
	modular_pow1(4, 13, 497) == int(math.pow(4,13)% 497)
	"""	
	c = 1
	ep = 0
	while True:
		ep += 1
		if ep > e:
			return c
		c = (b*c) % m
		
def modular_pow_no_repeat(b, m):
	"""
	"""	
	c = 1
	ep = 0
	X = []
	while True:
		ep += 1
		c = (b*c) % m		
		if c in X:
			return X
		X.append(c)
	
def modular_pow(b, m, N):
	"""
	This algorithm makes use of the identity
	(a·b) mod m = [(a mod m)·(b mod m)] mod m
	b: base, m: modulus, N: count
	"""	
	X = arr.array1(N)
	if m == 1:
		X[0] = 0
		return X
	c = 1
	X[0] = 1
	i = 1
	for ep in range(N-1):
		c = (c*b) % m
		X[i] = c
		i += 1
	return X
	
def modular_pow_r2l(b, e, m):
	"""
	modular_pow_r2l(4, 13, 497) == int(math.pow(4,13)% 497)
	"""	
	if m == 1:
		return 0
	r = 1
	b = b % m
	while e > 0:
		if e%2 == 1 :
			r = (r*b) % m
		b = (b*b)%m
		e = e>>1
	return r
	
def test_modular_pow(b, m, N):
	X = modular_pow(b, m, N)
	#print(X)
	Y = arr.array1(N)
	for i in range(N):
		Y[i] = int(math.pow(b, i)% m)
	return X, Y
	#print(Y)
	
def test1(b, m):
	N = modular_pow_no_repeat(b, m)
	X, Y = test_modular_pow(b, m, len(N)+1)
	print(N)
	print(X[1:])
	print(Y[1:])
	
def test4():
	A = random.randint(1, 10)
	B = random.randint(1, 5)
	C = random.randint(1, 10)
	D = random.randint(1, 10)
	
	A0 = A
	A1 = A+10
	B0 = B
	B1 = B+5
	C0 = C
	C1 = C+10
	D0 = D
	D1 = D+5
	
	i = 0
	for d in range(D0,D1+1):
		for c in range(C0,C1+1):
			for b in range(B0,B1+1):
				for a in range(A0,A1+1):
					i = i+1
					X, Y = test_modular_pow(a, b, c, d)
					if X != Y:
						print(a,b,c,d)
						print(X)
						print(Y)
						return
	print(i)
					
