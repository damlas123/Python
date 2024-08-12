def euclideanDistance(x,y):
  return (x**2+y**2)**0.5

points=[(1,5),(7,9),(5,4),(6,3)]
distance=[]
for e,d in points:
    distance.append(euclideanDistance(e,d))
min=distance[0]
for e in range(1,len(distance)):
  if min>distance[e]:
     min=distance[e]
 

print("the shortest way is:",min)