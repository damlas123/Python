l1=[5,8,9,7]
#l2=l1
l2=l1.copy()
l1[1]=10
print(l1)
print(l2)
#list kopyalama yapılırken l1 ve l2 aynı yeri gösterir c dilindeki pointerlar gibi ikisi aynı yeri gösterir bundan dolayı l1 değişince l2 de değişir
#eğer l2 değişssin istemiyorsak copy komutunu kullanarak liste yapılması gerek
#list concatenation iki listenin birleşik yazılmasına denir
l3=l1+l2
print(l3)
#l1.reverse()
print(l1[::-1])
print(l1)
#reverse fonk kullanılarak liste ters çevrilebilir ama bu listeyi l1[::-1] ile de ters çevrilir ve lsite eksi haline döner
y=sorted(l1)
print(y)
#küçükten büyüğe doğru sıralar sorted ama elemanların yeri böyle kalır
print(l1.sort())
#2. şekilde lsitenin sadece bu bloğunda listelenir sonra eski haline döner
