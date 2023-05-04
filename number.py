# import zd
# import math_zd.number as number
#
# import importlib
# importlib.reload(number)

from math import gcd as bltin_gcd
from math import gcd
import util.arr as arr
import math

def imp():
	global bltin_gcd, gcd, math
	from math import gcd as bltin_gcd
	from math import gcd
	import math
	
# copy rrr() to IDLE, run from there.
# import util.arr as arr
# import importlib
def rrr():
	importlib.reload(number)
	
	
def Wheel_factorization(n):
	"""
	>>> Wheel_factorization(10)
	[2, 5]
	"""
	X = []
	while (n%2) == 0:
		X.append(2)
		n = int(n/2)
		
	d = 3
	while d*d <= n:
		while (n%d) == 0:
			X.append(d)
			n = int(n/d)
		d += 2
	
	if n>1:
		X.append(n)
	
	return X
	
	
def coprime2(a, b):
    return bltin_gcd(a, b) == 1
	
# https://the-algorithms.com/algorithm/prime
def is_prime(number: int) -> bool:
    # precondition
    assert isinstance(number, int) and (
        number >= 0
    ), "'number' must been an int and positive"

    if 1 < number < 4:
        # 2 and 3 are primes
        return True
    elif number < 2 or not number % 2:
        # Negatives, 0, 1 and all even numbers are not primes
        return False

    odd_numbers = range(3, int(math.sqrt(number) + 1), 2)
    return not any(not number % i for i in odd_numbers)


def next_prime(value, factor=1, **kwargs):
    value = factor * value
    first_value_val = value

    while not is_prime(value):
        value += 1 if not ("desc" in kwargs and kwargs["desc"] is True) else -1

    if value == first_value_val:
        return next_prime(value + 1, **kwargs)
    return value
	
def find_all_divisors(n):
	"""
	>>> find_all_divisors(2*3*7)
	[1, 2, 3, 6, 7, 14, 21, 42]
	"""
	def powerset_mult_elements(X):
		Y = array1(len(X))
		ix = 0
		for x in X:
			if len(x) == 0:
				Y[ix] = 1
			else:
				Y[ix] = mult_list_elements(x)
			ix += 1
		return Y
	X = Wheel_factorization(n)
	P = powerset(X)
	D = list(set(powerset_mult_elements(P)))
	D.sort()
	return D


# https://stackoverflow.com/questions/32871539/integer-factorization-in-python	
def prime_factorization___(n):
    """
    >>> prime_factorization(2*2*3*3*5*7*11)
    [3, 3, 4, 7, 11, 5]
    """
	print("this function is buggy")
	return
	
    factors = []

    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for count in range(cycle_size):
                if factor > 1: break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)

            cycle_size *= 2
            x_fixed = x

        return factor

    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next

    return factors

	
def generate_exp_remainders(a, p, N):
	"""
	returns [a^1 % N, a^2 %N, ... a^p % N]
	>>> find_exp_remainders(2,4,10)
	[2,4,8,6]
	"""
	X = arr.array1(p)
	r = a % N
	X[0] = r
	p_1 = p-1
	for i in range(p_1):
		r1 = (r * a) % N
		r = r1
		X[i+1] = r
	return X
	
def generate_exp_mod_N(a, N):
	"""
	generate powers of a mod N, stop when remainder has been generated.
	"""
	r = a % N
	X = [r]
	while True:
		r1 = (r * a) % N
		r = r1
		if r in X:
			break
		X.append(r)
	return X	

# https://github.com/TheAlgorithms/Python/blob/master/blockchain/chinese_remainder_theorem.py
# Extended Euclid
def extended_euclid(a: int, b: int) -> tuple[int, int]:
    """
    >>> extended_euclid(10, 6)
    (-1, 2)
    >>> extended_euclid(7, 5)
    (-2, 3)
    """
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)


# Uses ExtendedEuclid to find inverses
def chinese_remainder_theorem(n1: int, r1: int, n2: int, r2: int) -> int:
    """
    >>> chinese_remainder_theorem(5,1,7,3)
    31
    Explanation : 31 is the smallest number such that
                (i)  When we divide it by 5, we get remainder 1
                (ii) When we divide it by 7, we get remainder 3
    >>> chinese_remainder_theorem(6,1,4,3)
    14
    """
    (x, y) = extended_euclid(n1, n2)
    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2
    return (n % m + m) % m


# ----------SAME SOLUTION USING InvertModulo instead ExtendedEuclid----------------


# This function find the inverses of a i.e., a^(-1)
def invert_modulo(a: int, n: int) -> int:
    """
    >>> invert_modulo(2, 5)
    3
    >>> invert_modulo(8,7)
    1
    """
    (b, x) = extended_euclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b


# Same a above using InvertingModulo
def chinese_remainder_theorem2(n1: int, r1: int, n2: int, r2: int) -> int:
    """
    >>> chinese_remainder_theorem2(5,1,7,3)
    31
    >>> chinese_remainder_theorem2(6,1,4,3)
    14
    """
    x, y = invert_modulo(n1, n2), invert_modulo(n2, n1)
    m = n1 * n2
    n = r2 * x * n1 + r1 * y * n2
    return (n % m + m) % m