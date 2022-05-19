# use of __init__
"""
For init.py:  https://stackoverflow.com/questions/448271/what-is-init-py-for
For setup.py: https://stackoverflow.com/questions/1471994/what-is-setup-py

"""
"""
The “self” keyword in the __init__() tells the python interpreter to make the variables 
part of the new object. So, if you use self.myvar = ‘foo’, then you’re new object will 
have a variable called myvar which equals ‘foo’. If you used myvar = ‘foo’ without the 
self keyword, the __init__ function would have a variable named myvar set to ‘foo’ which 
would be out of scope and lost when __init__ finished.
"""
class User(object):
    def __init__(self, something):
        print("User Init called.")
        self.something = something

    def method(self):
        return self.something 

class Student(User):
    def __init__(self, something):
        User.__init__(self, something)
        print("Student Init called.")
        self.something = something

    def method(self):
        return self.something 

my_object = Student('Jetty')

