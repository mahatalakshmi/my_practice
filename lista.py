n=input()

if not n[0:5].isalpha():
    print("invalid")
elif not n[5:9].isdigit():
    print("inalid")
elif not n[10].isalpha():
    print("invalid")
else: print("valid")    



    


