from stos import Stack
#rozwiązanie zagadnienia wieży z Hanoi metoda rekurencyjna z wykorzystaniem 3 stosów
def hanoi(stos1,stos2,stos3,n):
    #stos1=Stack()
    #stos2=Stack()
    #stos3=Stack()
    #n = stos1.size()
    if n == 0:
        return
    elif n == 1:
        stos3.push(stos1.pop())
        print('Ściągam z wieży 1 i kładę na wieżę 3')
    elif n == 2:
        stos2.push(stos1.pop())
        print('Ściągam z wieży 1 i kładę na wieżę 2')
        stos3.push(stos1.pop())
        print('Ściągam z wieży 1 i kładę na wieżę 3')
        stos3.push(stos2.pop())
        print('Ściągam z wieży 2 i kładę na wieżę 3')
    else:
        hanoi(stos1, stos3, stos2, n-1)
        stos3.push(stos1.pop())
        print('Ściągam z wieży 1 i kładę na wieżę 3')
        hanoi(stos2, stos1, stos3,n-1)

s1=Stack()
for i in range(1,4):
    s1.push(i)
s2=Stack()
s3=Stack()
n=s1.size()
print(s1,s2,s3)
hanoi(s1,s2,s3,n)
print(s1,s2,s3)