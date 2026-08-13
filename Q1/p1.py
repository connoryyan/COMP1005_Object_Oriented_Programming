class Layer:
    def __init__(self, size, flavour):
        self.size = size
        self.__flavour = flavour
        self.is_baked = False

    def __str__(self):
        return f'{self.size}" {self.__flavour} tier.'

    def set_flavour(self, flavour):
        if not self.is_baked:
            self.__flavour = flavour

    def get_flavour(self):
        return self.__flavour

    def bake(self):
        print(f"3, 2, 1... *Ding* The {self.__flavour} tier is ready.")
        self.is_baked = True


class Cake():
    def __init__(self):
        self.tiers = []

    def __str__(self):
        ret = f"A {len(self.tiers)} tier celebration cake made of:\n"
        for tier in self.tiers:
            ret += f"- {tier}\n"

        return ret

    def add_tier(self, tier):
        if not isinstance(tier, Layer):
            return
        if tier.is_baked:
            self.tiers.append(tier)
        else:
            print("I should bake this first.")


if __name__ == "__main__":
    layer_1 = Layer(11, "Vanilla")
    layer_2 = Layer(8, "Caramel")
    layer_3 = Layer(6, "Strawberry")
    cake = Cake()

    print(layer_1)
    print(layer_2)
    print(layer_3)

    cake.add_tier(layer_1)

    layer_1.bake()
    layer_2.bake()
    layer_3.bake()

    cake.add_tier(layer_1)
    cake.add_tier(layer_2)
    cake.add_tier(layer_3)

    print(cake)
