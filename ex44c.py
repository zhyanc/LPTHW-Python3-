class Parent(object):
    def altered(self):
        print("Parent altered()")

class Child(Parent):
    def altered(self):
        print("Child altered(): without - super()")
        super(Child, self).altered()
        print("Child altered(): with - super()")

dad = Parent()
son = Child()

dad.altered()
print("-" * 20 + "\n")
son.altered()
