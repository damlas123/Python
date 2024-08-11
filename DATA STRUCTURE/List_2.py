#For function usage for showing a list elements
notlar=[90,48,54,76]
for e in notlar:
    print(e)
#find avarage for a list
total=0
for e in notlar:
   total+=e

avg=total/len(notlar)
print("avarage :",avg)

#second way to show elements of a list
t=0
for e in range(len(notlar)):
    print(notlar[e])
#for avarage
for e in range(len(notlar)):
    t+=notlar[e]

av=t/len(notlar)
print("avarage:",av)
#to make an update in a list
for i in range(len(notlar)):
    notlar[i]+=5
    #we add all notes 5 points
print(notlar)