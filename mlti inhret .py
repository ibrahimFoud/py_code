class grandfather :
    def __init__(self , name , age ):
        self.name = name 
        self.age = age 

    def display(self):
        return f"Hello My Name is {self.name} and I in {self.age} Age "


class mather (grandfather) :
    def __init__(self , name , age , jop):
        super().__init__(name , age)
        self.jop = jop
    
    def display(self):
        
        return super().display() + f" and i work as {self.jop} "

class father (mather)  :
    def __init__(self , name , age , jop , task):
        super().__init__(name , age ,jop)
        self.task = task

    def display(self):
        
        return super().display() + f"and i have a task such as {self.task} "

class son (father , mather):
    def __init__(self , name , age , jop , task ,fun ):
        super().__init__(name , age , jop , task)
        self.fun = fun 

    def display(self):
        
        return super().display() + f"sure i will have fun such as {self.fun} "



son1 = son("ibrahim" , 19 , "N/A" , "N/A" , "coding")
print(son1.display())