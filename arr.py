# import zd
# import util.arr as arr
#
# import importlib
# importlib.reload(arr)

import numpy as np
from array import array

import util.tools as tools

#fn = 'f:\\tmp\\data.bin'

def imp():
	global np, array
	import numpy as np
	from array import array

# copy rrr() to IDLE, run from there.
# import importlib
def rrr():
	importlib.reload(arr)
	
def count(X):
	"""
	X is a list like [1, 0, 0, 3], returns [1, 2, 2, 1]
	"""
	C = array1(len(X))
	for ix, x in enumerate(X):
		C[ix] = X.count(x)
	return C
		
def hasDuplicates(X):
	"""
	X is a list like [1, 2, 3]
	"""
	for x in X:
		if X.count(x) > 1:
			return True
	return False
	
def hasDuplicatesInRows(T):
	rows = len(T)

	for row in range(rows):
		if hasDuplicates(T[row]):
			return row
	return -1

def hasDuplicatesInCols(T):
	rows = len(T)
	cols = len(T[0])

	for col in range(cols):
		C = getColumn(T, col)
		if hasDuplicates(C):
			return col
	return -1
	
def hasDuplicatesInRowsAndCols(X):
	if hasDuplicatesInRows(X) != -1:
		return True
	if hasDuplicatesInCols(X) != -1:
		return True
	return False	
	
def getColumn(X, col):
	rows = len(X)
	C = array1(rows)
	for i in range(rows):
		C[i] = X[i][col]
	return C
	
def array1(col):
	"""
	return a list like [[], [], []]
	"""
	return [ [] for i in range(col)]
	
def array2(row, col):
	"""
	return an array like [[[], []], [[], []], [[], []]]
	"""
	return [ array1(col) for i in range(row)]

def argv_to_array(*argv):
	X = []
	for arg in argv:
		X.append(arg)
	return X

def argv_to_tuple(*argv):
	return tuple(argv_to_array(*argv))



def process_array_row_col_data(arr, func):
	rows = len(arr)
	cols = len(arr[0])
	for row in range(rows):
		for col in range(cols):
			func(row, col, arr[row][col])
			
def process_array_data(arr, func):
	rows = len(arr)
	cols = len(arr[0])
	for row in range(rows):
		for col in range(cols):
			func(arr[row][col])		
			
def print_array_data(arr):
	rows = len(arr)
	cols = len(arr[0])
	for row in range(rows):
		for col in range(cols):
			tools.printf("%d\t", arr[row][col])	
		#tools.printf("%d\n", row)
		tools.printf("\n")

	

# input: a, b are both array (1D)
def find_scale(a, b, epislon):
	Na = int(a.shape[0])
	Nb = int(b.shape[0])
	if Na != Nb :
		return
	
	scale = 0
	for i in range(Na):
		if abs(b[i]) > epislon:
			t = a[i] / b[i]
			if abs(t) > abs(scale):
				scale = t
	
	return scale
			
	

def save_float32_bin(fn, x):
	# x = np.float32(x)			#float64(maybe any type) -> float32 conversion
	with open(fn, 'wb') as f:
		x.tofile(f)		# dtype=np.float32 doesn't work here, data conversion should be done separately.
	
def load_float32_bin(fn):
	with open(fn, 'rb') as f:
		return np.fromfile(f, dtype=np.float32)
		
def powerset(s):
	"""
	powerset([2, 6, 5, 7])
	"""
	X = []
	x = len(s)
	for i in range(1 << x):
		X.append([s[j] for j in range(x) if (i & (1 << j))])
	return X
		
def mult_list_elements(X):
	m = 1
	for x in X:
		m = m * x
	return m
		
def powerset_mult_elements(X):
	Y = array1(len(X)-1)
	ix = 0
	for x in X:
		if len(x) != 0:
			Y[ix] = mult_list_elements(x)
			ix += 1
	return Y
	

def test_text_format():
	aa = random_float(10)
	save_float('d:\\engine\\media\\tmp\\test.bin', aa)

# compare two arrays
def compare(a, b):
	sz = min(a.shape, b.shape)[0]
	random_indices = np.random.randint(0, sz, 10)
	print("random 10 results from both sides", random_indices)
	for i in random_indices:
		print(a[i], b[i])
	
	
	d = abs(a - b)
	print("max difference is ", max(d))	
	
def random_float(cnt):
	return np.random.random(cnt)	
	
#save to text file
def save_float(fn, x):
	np.savetxt(fn, x, fmt='%f')	
	
#load from text file, I guess data is like '3.242 2.324, ...'	
def load_float(fn):
	return np.loadtxt(fn,  dtype=float)	
	

def generate_random_integer_array_1D(MAX_NUMBER, cols):
	return np.random.randint(MAX_NUMBER, size=(cols)).tolist()
	
def generate_random_integer_array_2D(MAX_NUMBER, rows, cols):
	return np.random.randint(MAX_NUMBER, size=(rows, cols)).tolist()
	