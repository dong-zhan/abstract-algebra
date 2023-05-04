# abstract-algebra
abstract algebra

I just learned abstract algebra for a few days.
This is a toy tools in hope it's helpful to anyone who's learning the same thing :)

example outputs

>>> test_mul_mod_N(2, 12)
Multiplicative Mod 12
Set: [2, 4, 8]
Cayley table
X 2 4 8 
2 4 8 4 
4 8 4 8 
8 4 8 4 
is_associative = True
unique identity: (None) False
is_closed: True
Latin square property: False

>>> test_mul_mod_N(2, 5)
Multiplicative Mod 5
Set: [2, 4, 3, 1]
Cayley table
X 2 4 3 1 
2 4 3 1 2 
4 3 1 2 4 
3 1 2 4 3 
1 2 4 3 1 
is_associative = True
unique identity: (1) True
is_closed: True
Latin square property: True
