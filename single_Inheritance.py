class Sl:
    def display(self):
        print("Base Class")
class Dl(Sl):
    def derived(self):
        print("Derived Class")
obj=Dl()
obj.derived()
obj.display()