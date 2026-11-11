from datetime import datetime

class person:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def get_birth_year(self):
        current_year=datetime.now().year
        print( current_year-self.age )
    def base_info(self):
        print (f"name : {self.name}\nage : {self.age}  ")
    
        
class student(person):
    def __init__(self,age,name,st_id):
        super().__init__(age,name)
        self.st_id=st_id
    def showStudentInfo(self):
        super().base_info()
        print(self.st_id)

class teacher(person):
    def __init__(self,age,name,t_code,department):
        super().__init__(age,name)
        self.t_code=t_code
        self.department=department

class employee(person):
    def __init__(self,name:str,age:int):
        super().__init__(name,age)

s1=student("sina",18,3196)
t1=teacher("ali",28,313,"math")
e1=employee("sina",25)


s1.showStudentInfo()
s1.get_birth_year()