# constructor: constructor is used to set up some instance variable to have the proper initial values when object is created.
class Person:
    name = 'takib'
    x = 0

    def __init__(self, z):
        print('I am contructed', z)

    def getNumber(self):
        self.x = self.x + 1
        print('so far', self.x)

    def getName(self):
        print('My name is:', self.name)

    def __del__(self):
        print('I am destructed', self.x)


person1 = Person('Rakib')
person1.getName()
person1.getNumber()
person1.getNumber()
