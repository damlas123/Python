square=[]
for i in range(1,11):
 square.append(i*i)
print(square)
#second way
squares=[]
squares=[i*i for i in range(1,11)]
print(squares)
#for cube
def cube(x):
    return x*x*x

cubes=[cube(i) for i in range(1,11)]
print(cubes)
#second way
c=[]
for i in range(1,11):
    c.append(i*i*i)
print(c)
#find odd number in squares
odd_squares=[]
for i in square:
    if i%2==1:
     odd_squares.append(i)
print(odd_squares)
#find even number in cubes
even_cubes=[]
for i in cubes:
    if i%2==0:
     even_cubes.append(i)
print(even_cubes)