s={5,1,2,4,7,9}

def fun1(s1):
    '''s1.add(11) # adding the elements in set using add function
    print(s1)'''

    '''s1.clear()   # clear function in Set
    print(s1)'''

    '''s2=s1.copy()  #copy data one element to other element
    print(s2)'''

    '''s2={2,4,1,10,9,11}        #printing the different elements
    print(s1.difference(s2))'''

    '''s2={2,4,1,10,9,11}
    s1.difference_update(s2)  #printing different element but updated s1
    print(s1)'''

    '''s1.discard(7)       #Discarding(removing the elment)
    print(s1)'''

    '''s2={5,4,9,10}              #comman element will print
    print(s1.intersection(s2)) '''

    s2={5,4,9,10}
    s1.intersection_update(s2)
    print(s1)
fun1(s)
