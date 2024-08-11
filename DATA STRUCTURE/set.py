#setler listeler gibidir ama süslü parantez kullanılır köşeli değil
s={1,5,8,9}
print(type(s))
s.add(6)
s.remove(1)
s.discard(9)
print(s)
s2={5,7,9,12,52,47}
print(s.difference(s2))
print(s-s2)
print(s.symmetric_difference(s2)) #symmetric difference show 2 union set without intersection
print(s.intersection(s2)) # show 2 set intersection
y=s.union(s2)
print(y)
print(s.isdisjoint(s2)) #this function show there is a intersection in 2 set or not if it is , it gives false
print(s.issubset(s2)) #this show one of these set is subset other one 
print(s.issuperset(s2)) #tis show one of these set is super set other one