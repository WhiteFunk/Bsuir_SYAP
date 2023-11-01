class Task:
    a = 3
    b = 4
    
    def __init__(self, c,d):
        self.c = c
        self.d = d
    
    def first(self):
        a = "variable"
        print(a)
    
    def second(self):
        return self.a+self.b
        
    def third(self):
        return self.c**self.d
        
t = Task(5,6)
print(t.third())