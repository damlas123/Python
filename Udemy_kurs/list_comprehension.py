"""liste1=[1,2,3,4,5,6]
list2=list()
for i in liste1:
    list2.append(i)
print(list2)"""

"""liste1=[2,5,8,7,9,4]
list2=[i for i in liste1]
print(list2)"""

"""liste=[1,2,3,4,5]
l1=[2*i for i in liste]
print(l1)"""

l=[(1,2,3,4),(8,9),(65,47)]
l2=[x for i in l for x in i]
print(l2)