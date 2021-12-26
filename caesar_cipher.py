a="pyton"
b=''
for i in a:
    c=ord(i)+3
    if c>ord('z'):
        c=ord('a')+(c-122)-1
    x=chr(c)
    b=b+x   
print(b)    
