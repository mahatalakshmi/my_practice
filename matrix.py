a=[]
for i in range(3):
    b=[]
    for j in range(3):
        b.append(int(input()))
    a.append(b)
print(a)
for i in range(3):
    for j in range(3):
        if a[i][j]%2==0 and j==i:
            k=0
        elif a[i][j]%2!=0 and j==i:
            k=1
        elif j!=i and a[i][j]!=0:
            k=2
if k==0:
    print("Even") 
if k==1 :
    print("not even")
if k==2:
    print(False)                          
            


     


