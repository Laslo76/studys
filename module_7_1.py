#Bogushev V.V.
class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}.'


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        file_products = open(self.__file_name, "a")
        file_products.close()

    def get_products(self):
        file_products = open(self.__file_name, "r")
        products = file_products.read()
        file_products.close()
        return products

    def add(self, *products):
        assortment = self.get_products()

        for product in products:
            if product.name in assortment:
                print(f'Продукт {product.name} уже есть в магазине.')
            else:
                file_products = open(self.__file_name, "a")
                file_products.write(f'{str(product)}\n')
                file_products.close()


if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())