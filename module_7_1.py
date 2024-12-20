class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'
    def get_products(self):
        f = open(self.__file_name, 'r')
        ret_val = f.read()
        f.close()
        return ret_val

    def add(self, *products):
        all_products = self.get_products()
        for p in products:
            if p.name not in all_products:
                f = open(self.__file_name, 'a')
                f.write(f"{p}\n")
            else:
                print(F"Продукт {p.name} уже есть в магазине")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)

print(s1.get_products())