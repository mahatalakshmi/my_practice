n=int(input("enter"))
a=[]
for i in range(n):
    print("index",i)
    a.append(int(input()))
#bubble sort
'''for i in range(n):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t   
for i in range(n):
    print(i)'''
#linear search
#x=int(input())
#for i in range(n):
#    if(x==a[i]):
#        print("yep",i+1)
#        exit()
#else: print("nope")    
m=int(input())
n=int(input())
mat=[]
for row in range(m):
    rowv=[]
    for col in range(n):
        rowv.append(int(input()))
    mat.append(rowv)  
print(mat)      
