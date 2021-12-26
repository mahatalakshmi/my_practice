import re
email=input("enter email:").strip()
x=re.match("[a-zA-Z0-9]+@(gmail.com)",email) 
if x:
       username=email[:email.index('@')]
       mail=email[email.index('@')+1:]
       print("your username: {} \n your email: {}".format(username,mail))
else: 
    print("enter correct email") 
           