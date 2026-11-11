class user:
    def __init__(self,name,email,password):
        self.name=name
        self._email=email
        self.__password=password
    def get_password(self):
        return self.__password
    def set_password(self,new_password):
        self.__password=new_password

u2=user("mahdi","mahdi@gmail.com","313")
print(u2.get_password())
u2.set_password("07351952846")
print(u2.get_password())


