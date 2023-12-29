#def sum ( a , b):
   # sumation = a + b
    #print(sumation)


#def sum (a , b, c):
    #sumation = a + b + c    
    #print(sumation)



sum( 4 , 4 , 4)

print('_'*30)
print(" ")


def get_sum(datatype , *args):
    if datatype == "int":
        answer = 0
    
    if datatype == "str":
        answer  = ""

    for x in args :
        answer = answer + x
    print(answer)

get_sum("str", "ibrahim " ,"fouad") 

print('_'*30)
print(" ")


def add(a = None , b = None):
    if a != None and b ==   None :
        print(a)
    else:
        print (a + b)

add(5 , 10)
          
print('_'*30)
print(" ")


from multipledispatch import dispatch

@dispatch(int , int )
def product (num1  ,num1):
    result = num1 * num2
    print(result)


@dispatch(int , int , int)
def product (num1 , num2 , num3 ):
    result = num1 * num2 * num3
    print(result)
