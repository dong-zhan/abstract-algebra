abstract algebra<br /><br />This is a toy tools in hope it's helpful to anyone who's learning abstract algebra :)<br /><br />example outputs<br /><br />test_Sn(3)<br />S(3): [[], [[2, 3]], [[1, 2]], [[1, 2, 3]], [[1, 3, 2]], [[1, 3]]]<br />Cayley table<br /><table><br /><tr><br /><td>['XXX']</td><td>[]</td><td>[[2, 3]]</td><td>[[1, 2]]</td><td>[[1, 2, 3]]</td><td>[[1, 3, 2]]</td><td>[[1, 3]]</td></tr><br /><tr><br /><td>[]</td><td>[]</td><td>[[2, 3]]</td><td>[[1, 2]]</td><td>[[1, 2, 3]]</td><td>[[1, 3, 2]]</td><td>[[1, 3]]</td></tr><br /><tr><br /><td>[[2, 3]]</td><td>[[2, 3]]</td><td>[]</td><td>[[1, 3, 2]]</td><td>[[1, 3]]</td><td>[[1, 2]]</td><td>[[1, 2, 3]]</td></tr><br /><tr><br /><td>[[1, 2]]</td><td>[[1, 2]]</td><td>[[1, 2, 3]]</td><td>[]</td><td>[[2, 3]]</td><td>[[1, 3]]</td><td>[[1, 3, 2]]</td></tr><br /><tr><br /><td>[[1, 2, 3]]</td><td>[[1, 2, 3]]</td><td>[[1, 2]]</td><td>[[1, 3]]</td><td>[[1, 3, 2]]</td><td>[]</td><td>[[2, 3]]</td></tr><br /><tr><br /><td>[[1, 3, 2]]</td><td>[[1, 3, 2]]</td><td>[[1, 3]]</td><td>[[2, 3]]</td><td>[]</td><td>[[1, 2, 3]]</td><td>[[1, 2]]</td></tr><br /><tr><br /><td>[[1, 3]]</td><td>[[1, 3]]</td><td>[[1, 3, 2]]</td><td>[[1, 2, 3]]</td><td>[[1, 2]]</td><td>[[2, 3]]</td><td>[]</td></tr><br /></table><br /><br />test_additive_coset(6)<br />Z6:[0 1 2 3 4 5]<br />subgroup generated by <3>:[3, 0]<br />coset generated by 2·<3>:[5, 2]<br />coset generated by 4·<3>:[1, 4]<br /><br />test_multiplicative_coset(7)<br />U7:[1, 2, 3, 4, 5, 6]<br />subgroup generated by <2>:[2, 4, 1]<br />coset generated by 3·<2>:[6, 5, 3]<br /><br />test_additive_subgroup(6)<br />Z6:[0 1 2 3 4 5]<br /><0>[0]<br /><1>[1, 2, 3, 4, 5, 0]<br /><2>[2, 4, 0]<br /><3>[3, 0]<br /><4>[4, 2, 0]<br /><5>[5, 4, 3, 2, 1, 0]<br /><br />test_U(8)<br />Multiplicative Group of Integers Modulo 8 (U8)<br />Mod: 8<br />Set: [1, 3, 5, 7]<br />Cayley table<br />X 1 3 5 7 <br />1 1 3 5 7 <br />3 3 1 7 5 <br />5 5 7 1 3 <br />7 7 5 3 1 <br />is_associative = True<br />unique identity: (1) True<br />is_closed: True<br />Latin square property: True<br /><br />test_cyclic(2,6)<br />a=2 and N=6 are coprime: False<br />so, a=2 has modular multiplicative inverse: False<br />cyclic group <2> Mod: 6<br />Set: [2, 4]<br />Cayley table<br />X 2 4 <br />2 4 2 <br />4 2 4 <br />is_associative = True<br />unique identity: (4) True<br />is_closed: True<br />Latin square property: True<br /><br />test_cyclic(2,5)<br />a=2 and N=5 are coprime: True<br />so, a=2 has modular multiplicative inverse: True<br />cyclic group <2> Mod: 5<br />Set: [2, 4, 3, 1]<br />Cayley table<br />X 2 4 3 1 <br />2 4 3 1 2 <br />4 3 1 2 4 <br />3 1 2 4 3 <br />1 2 4 3 1 <br />is_associative = True<br />unique identity: (1) True<br />is_closed: True<br />Latin square property: True<br />