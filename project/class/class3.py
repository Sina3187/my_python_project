class user:
    count=0
    def __init__(self,name,family):
        self.name=name
        self.family=family
        user.count+=1
    @classmethod
    def show_coint(cls):
        print(f" count : {cls.count}")

u1=user("sina","rostami")
u2=user("soheil","rostami")
