import numpy as np
from scipy import linalg
import time
import random
import matplotlib.pyplot as plt
#analiza eksperymentalna wydajności/złożoności obliczeniowej funkcji solve
def analiza(n): #n-licza niewiadomych w równaniu
    a=[]
    b=[]
    for j in range(n):
        wsp_j=[]
        for i in range(n):
            p_i=random.randrange(100)
            wsp_j.append(p_i)
        a.append(wsp_j)
    #print(a)
    for k in range(n):
        g_k=random.randrange(100)
        b.append(g_k)
    #print(b)       
    c=np.array(a)
    d=np.array(b)
    start=time.time()
    x=linalg.solve(c,d)
    end=time.time()
    return (end-start)
print(analiza(180))

n=[10,100,  1000,  2000,  3000,  4000] #z analizy wykresu wynika, że złożoność oobliczeniowa jest wykładnicza
y=[]
for i in range(len(n)):
    y.append(analiza(n[i]))
f=plt.figure()
plt.plot(n,y,'ro')
plt.show()

print('{} \t {} \t'.format('N','T'))
for k in range(len(y)):
    print('{} \t {} \t'.format(n[k],y[k]))