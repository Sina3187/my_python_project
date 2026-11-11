class ShoppingCart:
    def __init__(self,shopping_id:int,name:str):
        self.shopping_id=shopping_id
        self.name=name
        self.items=[]
    def add_item(self,item):
        self.items.append(item)
    def __str__(self):
        return f" name : {self.name} \n SoppingId : {self.shopping_id} \n items : {self.items} \n {80*"-"}"
    def __eq__(self,obj2):
        return self.items==obj2.items

s1=ShoppingCart(1387,"sina")
s1.add_item("ball")
s1.add_item("book")

s2=ShoppingCart(313,"soheil")
s2.add_item("laptop")
s2.add_item("book")
s2.add_item("pen")


print(s1==s2)












