class Product:
    def __init__(self, name):
        self.name = name if name else None

    def __str__(self):
        return f"{self.name}"

class pc(Product):
    def __init__(self, **args):
        super().__init__(args.get("name"))
        self.__cpu = args.get("cpu")
        self.__ram = args.get("ram")
    
    def __str__(self):
        return f"""Computer:
    Name: {self.name}
    Procesor: {self.__cpu}
    Ram: {self.__ram} GB
    """
    
class monitor(Product):
    def __init__(self, **args):
        super().__init__(args.get("name"))
        self.__resolution = args.get("resolution")
        self.__diagonal_length = args.get("diagonal_length")
    
    def __str__(self):
        return f"""Monitor:
    Name: {self.name}
    Resolution: {self.__resolution[0]}x{self.__resolution[1]}
    Diagonal Length: {self.__diagonal_length} inches
    """

class keyboard(Product):
    def __init__(self, **args):
        super().__init__(args.get("name"))
        self.__technology = args.get("technology")
    
    def __str__(self):
        return f"""Keyboard:
    Name: {self.name}
    Technology: {self.__technology}
    """

class hamster(Product): # Hamter / Hamster he identifies under different pronounces
    def __init__(self, **args):
        super().__init__(args.get("name"))
        self.__technology = args.get("technology")
    
    def __str__(self):
        return f"""Hamter/Mouse/Hamter:
    Name: {self.name}
    Technology: {self.__technology}
    """

class Factory:
    product_type = ["pc","monitor","keyboard","hamster"]
    
    @staticmethod
    def produce(**args):
        if args.get("type").lower() in Factory.product_type:
            return globals()[args["type"].lower()](**args)

products = []

products.append(Factory.produce(type = "Pc",name = "Babičky PC",cpu = "Zinger Chicken",ram = 16))
products.append(Factory.produce(type = "MoNiTor",name = "Azus",diagonal_length = 125,resolution = (1280,720)))
products.append(Factory.produce(type = "keyBOARD",name = "LogiTek",technology = "wireless"))
products.append(Factory.produce(type = "HamsteRs",name = "Pablo",technology = "cable"))

for product in products:
    print(product)