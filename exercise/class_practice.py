class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
class Student(Person):
    def __init__(self, first_name, last_name, gpa, classes = []):
        super().__init__(first_name, last_name)
        self.gpa = gpa
        self.classes = classes
    
    def update_gpa(self, gpa):
        self.gpa = gpa


class Teacher(Person):
    def __init__(self, first_name, last_name, tenure, subject):
        super().__init__(first_name, last_name)
        self.tenure = tenure
        self.subject = subject
    
    def add_students(self, students):
        self.students = students 

class Food:
    def __init__(self, name, healthy, price):
        self.name = name
        self.healthy = healthy
        self.price = price


class ShoppingList:
    def __init__(self, shopping_list=[]):
        self.shopping_list = shopping_list

    def add_to_list(self, name, healthy, price):
        food = Food(name, healthy, price)
        self.shopping_list.append(food)
    
    def unhealthy_list(self):
        healthy = 0
        unhealthy = 0
        for item in self.shopping_list:
            if item.healthy is True:
                healthy += 1
            else:
                unhealthy += 1

        if healthy > unhealthy:
            print("items on the list are healthy")
        elif healthy < unhealthy:
            print("items on the list are unhealthy")
        else:
            print("choose healthy or unhealthy")




    def view_list(self):
        total = 0
        for item in self.shopping_list:
            print(item.name, item.price)
            total += item.price
        print(total)




# justin = Student('Justin', 'Sarraga', 4.0, ['web development'])
# print(justin.first_name)
# print(justin.gpa)
# justin.update_gpa(2.3)
# print(justin.gpa)

apple = Food('apple',True,1.0)
#print(apple.name, apple.healthy, apple.price)
shoplist = ShoppingList()
#print(shoplist.shopping_list)
shoplist.add_to_list('apple',True, 1.0)
shoplist.add_to_list('pinapple',True, 2.0)
shoplist.add_to_list('carrot',True, 3.0)
shoplist.add_to_list('banana',True, 4.0)
shoplist.add_to_list('banana',True, 4.0)
shoplist.add_to_list('bacon',False, 6.0)
shoplist.add_to_list('pizza',False, 8.0)
shoplist.add_to_list('hotdog',False, 10.0)
shoplist.add_to_list('icecream',False, 12.0)
#print(shoplist.shopping_list)
#print(shoplist.shopping_list[0])
shoplist.view_list()
shoplist.unhealthy_list()

