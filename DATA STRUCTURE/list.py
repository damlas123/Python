'''notlar=[100,90,65,40]
print(notlar[1])'''
#listelerde c dilinde olduğu gibi ilk index 0 olarak alınır
#listelerde her türden eleman olabilir
l1=["a","b",1,5,8.5,6.7]
print(l1[:])
#len listenin uzunluğunu bulmak için kullanılır
x=len(l1)
print(x)
#append listenin osnuna tek bir eleman ekler
l1.append(60)
print(l1[:])
#extend lsitenin sonuna istenildiği kadar eleman ekler
l1.extend([100,68,79])
print(l1[:])
#insert spesifik indexe eleman eklemek için kullanılır
l1.insert(4,44)
print(l1[:])
#remove listeden eleman silmek için kullanılır
l1.remove(60)
print(l1[:])
#pop önce silinen elemanı döndürür sonra siler(burada neden döndürmedi anlamadım)
l1.pop(1)
print(l1[:])
#count girilen elemanın kaç tane olduğunu söyler
print(l1.count(1))