# The __init__() function is called automatically every time
# the class is being used to create a new object.
# class Person:
#     def __init__(self, fname, lname):
#         self.fname=fname
#         self.lname=lname

# Method

    # def printname(self):
    #     print(self.fname, self.lname)


# To keep the inheritance of the parent's __init__() function,
# add a call to the parent's __init__() function:

# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)

# By using the super() function, you do not have to use the name of the parent element,
# it will automatically inherit the methods and properties from its parent.

# Add a property called graduationyear to the Student class:

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear=year

# If you add a method in the child class with the same name as a function
# in the parent class, the inheritance of the parent method will be overridden.

    # def welcome(self):
    #     print('Welcome', self.fname, self.lname)

#
# x=Student('John', 'Dan', 2022)
