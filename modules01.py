
import modules1






calc.a = 10   
print(calc.a)   


import calc  

print(calc.a)   

 
print('-------------------------------')



from small import a,b  

print(a) #1
print(b)  #[1,2]

a = 20  
b[0] =15 

print(a)   #20     
print(b)   #[15,2]

import small   

print(small.a)   #1
print(small.b)   #[15,2]
