class Student:
    def __init__(self):
        self._name = "ranjan"

    def _funName(self):      # protected method
        return "C2H3CL"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())
