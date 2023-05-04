# abstract-algebra <br>
abstract algebra<br>

I just learned abstract algebra for a few days.<br>
This is a toy tools in hope it's helpful to anyone who's learning the same thing :)<br>

example outputs<br>
<br>
>>> test_mul_mod_N(2, 12)<br>
Multiplicative Mod 12<br>
Set: [2, 4, 8]<br>
Cayley table<br>
X 2 4 8 <br>
2 4 8 4 <br>
4 8 4 8 <br>
8 4 8 4 <br>
is_associative = True<br>
unique identity: (None) False<br>
is_closed: True<br>
Latin square property: False<br>
<br>
>>> test_mul_mod_N(2, 5)<br>
Multiplicative Mod 5<br>
Set: [2, 4, 3, 1]<br>
Cayley table<br>
X 2 4 3 1 <br>
2 4 3 1 2 <br>
4 3 1 2 4 <br>
3 1 2 4 3 <br>
1 2 4 3 1 <br>
is_associative = True<br>
unique identity: (1) True<br>
is_closed: True<br>
Latin square property: True<br>
