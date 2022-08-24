import os
x=input("Enter the mobile number +91")
print(x)
if len(x)==10:
    if(x[0]>='6' and x[0]<='9'):
        print("Correct input")
        pass
    else:
        print("Invalid Input")
        os.abort()
    for i in x:
        if i>'0'and i<'9':
            pass
        else:
            print("Invalid input,enter 0 to 9 number")
            os.abort()
    

else:
    print("Length should be 10")
    os.abort()
