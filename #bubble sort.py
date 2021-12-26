#bubble sort
a=[10,2,6,9,17,1]
for i in range(len(a)):
    for j in range(i+1,len(a)):
          if a[i]>a[j]:
              emp=a[i]
              a[i]=a[j]
              a[j]=emp
print(a)              