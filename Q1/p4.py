class Product:
    def __init__(self, ID, rank, name=None):
        self.ID = ID
        self.__rank = 0
        self.set_rank(rank)
        self.name = name

    def get_rank(self):
        return self.__rank

    def set_rank(self, rank):
        if 1 <= rank <= 10:
            self.__rank = rank
        else:
            self.__rank = 0

    def __str__(self):
        if self.name is not None:
            return (f"Product ID: {self.ID}, Rank: {self.__rank}, "
                    f"Name: {self.name}")
        else:
            return f"Product ID: {self.ID}, Rank: {self.__rank}"


class Order:
    def __init__(self):
        self.__items = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.__items.append(product)

    def top_10_product_count(self):
        count = 0

        for product in self.__items:
            if 1 <= product.get_rank() <= 10:
                count += 1

        return count

    def __str__(self):
        return (
            f"Number of items: {len(self.__items)}\n"
            f"Number of top 10 products: {self.top_10_product_count()}"
        )


product1 = Product("P507", 2)

product2 = Product(
    "P488",
    -5,
    "Water Bottle"
)

my_order = Order()

my_order.add_product(product1)
my_order.add_product(product2)

print(my_order)
