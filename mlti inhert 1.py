class preson :
    def __init__(self , name , age):
        self.name = name 
        self.age = age 

    def display(self):
        return f"Your Name is {self.name } And your Age is {self.age}"

class eng (preson):
    
    def __init__(self , name ,age , career):
        super().__init__(name , age)
        self.career = career

    def display(self):
        return f"Your Name is {self.name } And your Age is {self.age} And your career is{self.career}"

class sup_eng(eng):
    def __init__(self , name , age , career , department):
        super().__init__(name , age ,career)
        self.department = department

    def display(self):
        return f"Your Name is {self.name } And your Age is {self.age} And your career is{self.career} And {self.department}"

class proggrammer(eng , preson):
    def __init__(self , name , age , career , language):
        super().__init__(name , age , career)
        self.language = language

    def display(self):
        return f"Your Name is : {self.name } And your Age is : {self.age} And your career is : {self.career} And the language is : {self.language}"





ibrahim = sup_eng("ibrahim" , 19 , "data science" , "python" )
print(ibrahim.display()) 
print("-"* 30)
kareem = proggrammer("ibrahim" , 19 , "data science" , "python" )
print(kareem.display())