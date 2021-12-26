n=int(input())
a=[]
b=[]
c=[]
sum1,sum2=0,0
for i in range(n):
    a.append(int(input()))
for i in range(n):
    if(a[i]>0):
        b.append(a[i])
    else:
        c.append(a[i]) 
print(b)
print(c)   
for i in range(len(b)):
    sum1=sum1+b[i]
for i in range(len(c)):
    sum2=sum2+c[i] 
print(sum1)
print(abs(sum2))                 



