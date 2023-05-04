# import zd
# import abs_alg.abs_alg as aa
#
# import importlib
# importlib.reload(aa)

# kerl-pyaa.pdf
# Lect2-04web.pdf
# E:\3d techs\math\Abstract Algebra\Finite Group -- from Wolfram MathWorld.pdf

def rrr():
	importlib.reload(aa)
	
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import util.arr as arr
import util.tools as tools

import math_zd.number as number


# if np,pd,plt is needed for console, copy imp() function to console, then run imp() in console  --> plot.imp() doesn't work.
def imp():
	global np, pd, plt, arr, tools
	import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt
	
	import util.arr as arr
	import util.tools as tools

def find_identity(X, binary_operation):
	"""
	X is a set
	find_identity([0, 1, 2], lambda x,y : (x+y) % 3)
	find_identity([0, 1, 2], lambda x,y : (x*y) % 3)
	"""
	for idd in X:
		isIdentity = True
		for x in X:
			if binary_operation(idd, x) != x:
				isIdentity = False
				break
		if isIdentity:
			return idd
	return None
	
def find_inverse(x, X, e, binary_operation):
	"""
	x is an element in set X
	X is a set
	e is identity
	find_inverse(1, [0, 1, 2], 0, lambda x,y : (x+y) % 3)
	"""
	for xi in X:
		if e == binary_operation(x, xi):
			return xi
	return None
	
def find_all_inverses(X, e, binary_operation):
	"""
	see test_find_all_inverses()
	"""
	IX = arr.array1(len(X))
	for ix, x in enumerate(X):
		inv = find_inverse(x, X, e, binary_operation)
		IX[ix] = inv
		#tools.printf("%d -> %d\n", x, inv)
		#if inv != None:
			#print(x)
	return IX
	

def has_Latin_Square_Property(X):
	"""
	every entry in column is different, and every entry in row is different
	"""
	return not arr.hasDuplicatesInRowsAndCols(X)
	
def count_inverse(X, e, binary_operation):
	"""
	X is a set, e is identity
	count_inverse([0, 1, 2, 3], 0, lambda x,y : (x+y)%4)
	"""
	IX = arr.array1(len(X))
	for i, a in enumerate(X):
		IX[i] = 0
		for b in X:
			ab = binary_operation(a, b)
			ba = binary_operation(b, a)
			if ab == e and ba == e:
				#print(a, b, ab, ba, e)
				IX[i] = IX[i]+1
	return IX
	
# TODO: vectorization
def is_associative(X, binary_operation):
	"""
	X is a set
	is_associative([2, 3, 4], lambda x,y : x-y)
	is_associative([2, 3, 4], lambda x,y : x+y)
	"""
	for a in X:
		for b in X:
			for c in X:
				ab = binary_operation(a, b)
				d1 = binary_operation(ab, c)
				bc = binary_operation(b, c)
				d2 = binary_operation(a, bc)
				if d1 != d2:
					#tools.printf("a=%d,b=%d,c=%d, ab=%d, d1=%d, bc=%d, d2=%d\n", a, b, c, ab, d1, bc, d2)
					return False
	return True
	
def is_closed(X, binary_operation):
	"""
	X is a set
	is_closed([0, 1, 2, 3, 4, 5], lambda x,y : (x+y) % 6)
	"""
	for a in X:
		for b in X:
			ab = binary_operation(a, b)
			if not ab in X:
				return False
	return True
	
def generate_Cayley_table(X, binary_operation):
	"""
	X is a set
	generate_Cayley_table([0, 1, 2, 3], lambda x,y : (x+y) % 4)
	generate_Cayley_table([1, 3, 7, 9], lambda x,y : (x*y) % 10)
	"""
	rows = len(X)
	cols = rows
	N = cols
	T = arr.array2(rows, cols)
	
	for irow, row in enumerate(X):
		for icol, col in enumerate(X):
			#print(irow, icol, row, col, binary_operation(row, col))
			T[irow][icol] = binary_operation(row, col)		
			
	return T
	
def generate_printable_Cayley_table(T, X):
	"""
	T is Cayley table
	X is a set
	add first row and first column into table, the top left should be the binary operation.
	"""
	rows = len(T) + 1
	cols = len(T[0]) + 1
	PT = arr.array2(rows, cols)
	
	for irow, row in enumerate(T):
		for icol, col in enumerate(T):
			PT[irow+1][icol+1] = T[irow][icol]	
			
	for i, ix in enumerate(T):
		PT[0][i+1] = X[i]
		PT[i+1][0] = X[i]
	
	#PT[0][0] = 0
	return PT
			
def print_Cayley_table(T, delimitor = ' '):
	"""
	T is printable Cayley table (Cayley table dimension extended by 1 for extra first row and first column)
	"""
	rows = len(T) + 1
	cols = len(T[0]) + 1
	
	for irow, row in enumerate(T):
		for icol, col in enumerate(T):
			t = T[irow][icol]
			if irow == 0 and icol == 0:
				tools.printf("X%c", delimitor)
			else:
				tools.printf("%d%c", t, delimitor)
		tools.printf("\n")
			
	
def Z(start, N):
	return np.arange(start,N,1)
		
def test_Carley_table2():
	binary_operation = lambda x,y : (x*y) % 10
	X = number.generate_exp_remainders(2, 4, 10)
	print(X)
	X = generate_Cayley_table(X, binary_operation)
	X = np.array(X)
	print(X)
	
def test_Carley_table1():
	binary_operation = lambda x,y : (x*y) % 10
	X = [1, 3, 7, 9]
	X = generate_Cayley_table(X, binary_operation)
	X = np.array(X)
	print(X)
	
def test_Carley_table(N):
	binary_operation = lambda x,y : (x+y) % N
	X = generate_Cayley_table(Z(N), binary_operation)
	X = np.array(X)
	print(X)
	
def test_find_all_inverses():
	binary_operation = lambda x,y : (x*y) % 10
	X = number.find_exp_remainders(2,4,10)
	identity = find_identity(X, binary_operation)
	IX = find_all_inverses(X, identity, binary_operation)	
	return X, IX

def test_mul_mod_N(a, N):
	"""
	this shows if N is prime, T is a group
	reference: The Euler-Fermat Theorem, Version 1.0
	reference: https://www.youtube.com/watch?v=TYb9NGFYx6U&list=PLKXdxQAT3tCuWdCHOz-bdm8nDsDI48yga&index=21

	"""
	binary_operation = lambda x,y : (x*y) % N
	
	#X = Z(1, N)
	X = number.generate_exp_mod_N(a, N)
	
	T = generate_Cayley_table(X, binary_operation)
	T = np.array(T)
	
	#tools.printf("Multiplicative Mod %d\nSet: ", N)
	tools.printf("Multiplicative Mod %d\nSet: ", N)
	print(X)
	
	print("Cayley table")
	
	PT = generate_printable_Cayley_table(T, X)
	print_Cayley_table(PT)
	
	ia = is_associative(X, binary_operation)
	tools.printf("is_associative = %s\n", ia)
	
	identity = find_identity(X, binary_operation)
	#tools.printf("identity = %s\n", str(identity))
	
	INV = count_inverse(X, identity, binary_operation)
	cols = len(X)
	uniqueIdentity = True
	cnt = INV.count(1)
	if cnt != cols:
		uniqueIdentity = False
	
	tools.printf("unique identity: (%s) %s\n", identity, uniqueIdentity)	
	
	tools.printf("is_closed: %s\n", is_closed(X, binary_operation))
	
	tools.printf("Latin square property: %s\n", has_Latin_Square_Property(T.tolist()))
	
	#tools.printf("N must be prime, in order for everything to be True\n")