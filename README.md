abstract algebra<br /><br />This is a toy tools in hope it's helpful to anyone who's learning the same thing :)<br /><br />example outputs<br /><br />test_cyclic(2,6)<br />a=2 and N=6 are coprime: False<br />so, a=2 has modular multiplicative inverse: False<br />cyclic group <2> Mod: 6<br />Set: [2, 4]<br />Cayley table<br />X 2 4 <br />2 4 2 <br />4 2 4 <br />is_associative = True<br />unique identity: (4) True<br />is_closed: True<br />Latin square property: True<br /><br /><br />test_cyclic(2,5)<br />a=2 and N=5 are coprime: True<br />so, a=2 has modular multiplicative inverse: True<br />cyclic group <2> Mod: 5<br />Set: [2, 4, 3, 1]<br />Cayley table<br />X 2 4 3 1 <br />2 4 3 1 2 <br />4 3 1 2 4 <br />3 1 2 4 3 <br />1 2 4 3 1 <br />is_associative = True<br />unique identity: (1) True<br />is_closed: True<br />Latin square property: True<br />