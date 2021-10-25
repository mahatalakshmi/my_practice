while True:
    num1=int(input())
    opp=input()
    num2=int(input())
    if opp=='add':
        print(num1,'+',num2,'=',num1+num2)
    elif opp=='sub':
        print(num1,'-',num2,'=',num1-num2)
    elif opp=='mul':
        print(num1,'*',num2,'=',num1*num2) 
    elif opp=='div':
        print(num1,'/',num2,'=',num1/num2)
    else:
         print("enter correctly")  
         continue   
    conc=input("want to continue")
    if conc=='yes':
        continue
    else:
        break
print("done")                 
