class Outer:
    def __init__(self):
        self.name = "Outer"

    class Inner:
        def __init__(self):
            self.name = "Inner"
        
        def display(self):
            print("This is the inner class")

outer = Outer()
print(outer.name)

inner = outer.Inner()
print(inner.name)
inner.display()