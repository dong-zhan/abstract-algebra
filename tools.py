# import zd
# import util.tools as tools
#
# import importlib
# importlib.reload(tools)

import numpy as np
from array import array

import util.arr as arr

def imp():
	global np, array
	import numpy as np
	from array import array

# copy rrr() to IDLE, run from there.
# import util.arr as arr
# import importlib
def rrr():
	importlib.reload(tools)
	
def printV(v):
	# To not add a newline to the end of the string: print('.', end='')   
	# To not add a space between all the function arguments you want to print:	print('a', 'b', 'c', sep='')
	print(v, sep ='', end='')
	
def print_XY_V(x, y, v):
	print(v, sep ='')	

	
def printf(fmt, *argv):
	print(fmt % arr.argv_to_tuple(*argv) , sep ='', end='')	
