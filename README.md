abstract algebra

This is a toy tools in hope it's helpful to anyone who's learning the same thing :)

example outputs

test_cyclic(2,6)
a=2 and N=6 are coprime: False
so, a=2 has modular multiplicative inverse: False
cyclic group <2> Mod: 6
Set: [2, 4]
Cayley table
X 2 4 
2 4 2 
4 2 4 
is_associative = True
unique identity: (4) True
is_closed: True
Latin square property: True


test_cyclic(2,5)
a=2 and N=5 are coprime: True
so, a=2 has modular multiplicative inverse: True
cyclic group <2> Mod: 5
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
