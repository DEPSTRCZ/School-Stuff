class Product:
    def __init__(self, name):
        self.name = name if name else None

    def __str__(self):
        return f"{self.name}"

class PC(Product):
    def __init__(self, **kwargs):
        print(kwargs["name"])
    
class Monitor(Product):
    pass

class Keyboard(Product):
    pass

class Mouse(Product):
    pass

class Factory:
    pass