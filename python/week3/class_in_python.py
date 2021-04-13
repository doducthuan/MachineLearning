class Person:
    name=''
    def setName(self, name):
        self.name=name
    def getName(self):
        return self.name
person=Person()
person.setName('Alex')
print(person.getName())
