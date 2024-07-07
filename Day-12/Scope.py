"""This  is created for the purpose exploring scopes"""

def my_function():
    counter = 0;
    if len(name)>0: # type: ignore
        counter+=1
    print(counter)
    
print(counter) #type: ignore

#This two counter prints are used to elaborate about Local scope
#meaning that variables declared inside function they are only usable inside the function
