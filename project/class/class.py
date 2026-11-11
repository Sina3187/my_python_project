class student:
    def __init__(self,name,family,number):
            self.name=name
            self.family=family
            self.number=number
    def __str__(self):
        return (f"name : {self.name} \nfamily : {self.family}  \nnumber : {self.number}\n{98*"-"}")

s1=student("mahdi","ghasemi","0904")
s2=student("sina","rostami","0996")
print(s1)
print(s2)


