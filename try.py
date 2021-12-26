n = int(input())
b = int(input())
s = []

while (n>0):
    a = n%10
    n//=10
    s.append(a)
print(s)
add=0
orig=0
check =1

for i in range(len(s)):
    add+=s[i]**len(s)
    print(add)
    orig+=s[i]*(b**i)
    print(orig)
    if(s[i]>b-1):
        print('Invalid')
        check = 0
        break
if(check):
    if(add==orig):
         print('Yes')
    else: 
        print ('No')

