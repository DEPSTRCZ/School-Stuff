class Equation():
    def __init__(self, a ,b):
        self.a = a
        self.b = b

    def solve(self):
        return (-self.a/self.b)
    
    def __str__(self):
        try:
            solve = self.solve()
        except ZeroDivisionError:
            return "No solution"
        except:
            return "Something went wrong"
        return f"x = {solve}"
    
test = Equation(10, 5)
print(test)