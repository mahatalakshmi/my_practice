
"""n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="") #if you wnat numbers then replace * with j;)
    print("\n")"""

"""n=int(input())
x=1
for i in range(1,n+1):
    for s in range(1,49-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(x,end=" ") 
        x=x+1 #if you want with * then replace x with * and remove x variables
       #if ypu want a pattern like 1 \n 2 2  \n 3 3 3 then replace x with i 
        #if you want a pattern like 1 \n 1 2  \n 1 2 3 then replace x with j 
          
    print("\n") """

"""n=int(input())
num=69 #assii value for printing the letters
ch=chr(num)

for i in range(1,n+1):
    for s in range(1,49-i):
        print(" ",end="")
    for j in range(1,i+1):
        ch=chr(num)
        print(ch,end=" ") 
    num=num+1    
        
    print("\n")   """
n=int(input())
num=69 #assii value for printing the letters
ch=chr(num)

for i in range(1,n+1):
    
    for j in range(1,i+1):
        ch=chr(num)
        print(ch,end=" ") 
        num=num+1    
        
    print("\n")   

