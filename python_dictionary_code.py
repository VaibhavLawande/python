d={1:"abc",2:"mno",3:"pqr",4:"xyz"}

def fun1(d1):

    '''d1.clear() # clear the dictonary function 
    print(d1)'''

    '''d2=d1.copy() #copy dict.1 to dict2
    print(d2)'''
    
    '''n="Vaibhav"          #fromkeys function in dict
    d2=dict.fromkeys(d1,n)
    print(d2)'''

    '''print(d1.get(4))'''   #get func in dict

    '''print(d1.items())''' #items function in Dict

    '''print(d1.keys())'''  #printing keys in dict.

    '''print(d1.pop(1))      #Poping the 1 keys Value
    print(d1)  '''           #remaining elements printing

    '''print(d1.popitem())''' # removing the last item of the dictionary

    '''d2=d1.setdefault(5)   #set default it will print value of key
    print(d2)'''

    '''d3={20:"Vaibhav"}#update function in dict,we can update the dict here
    d1.update(d3)
    print(d1)'''

    '''print(d1.values())''' #printing the values of dict.
    
fun1(d)
