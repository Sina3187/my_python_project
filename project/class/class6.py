class person:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def base_info(self):
        print (f"name : {self.name}\nage : {self.age}  ")
    
class student(person):
    def __init__(self,name,age,st_id):
        super().__init__(name,age)
        self.st_id=st_id
    def get_info(self):
        return(f"st_id : {self.st_id}")

class teacher(person):
    def __init__(self,name,age,t_code,department):
        super().__init__(name,age)
        self.t_code=t_code
        self.department=department
    def get_info(self):
        return(f"t_code : {self.t_code}")

class employee(person):
    def __init__(self,name:str,age:int,e_id):
        super().__init__(name,age)
        self.e_id=e_id
    def get_info(self):
        return(f"e_id : {self.e_id}")

s1=student("sina",18,3196)
t1=teacher("ali",28,313,"math")
e1=employee("sina",25,595)

people=[s1,t1,e1]
for person in people:
    print(person.get_info())



