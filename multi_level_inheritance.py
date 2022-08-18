class b1:
    def __init__(self):
        print("Main Base Class")
class b2(b1):
    def __init__(self):
        print("Derived class 1")
    def displays(self):
        print("SUB CLASS")
class b3(b2):
    def __init__(self):
        print("Derived class 2")
    def dis(self):
        print("derived class ")
x = b3()
x.dis()
x.displays()
print(b2())
z = b1()