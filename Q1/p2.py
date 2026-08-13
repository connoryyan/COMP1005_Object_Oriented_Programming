import math


class Wax:
    def __init__(self, type):
        self.__type = type
        self.__burn_time = self.calculate_burn_time()

    def calculate_burn_time(self):
        if self.__type == "Bee":
            return 1.1
        elif self.__type == "Paraffin":
            return 1.2
        elif self.__type == "Soy":
            return 1.4
        else:
            return 1.7

    def get_burn_time(self):
        return self.__burn_time

    def __str__(self):
        return f"Wax type: {self.__type}, Burn time: {self.__burn_time}"


class Wick:
    def __init__(self, length):
        self.__length = length
        self.__burn_time = self.calculate_burn_time()

    def calculate_burn_time(self):
        return round(self.__length * math.pi, 2)

    def get_burn_time(self):
        return self.__burn_time

    def __str__(self):
        return f"Wick length: {self.__length} cm, Burn time: {self.__burn_time}"


class Candle:
    def __init__(self, size, wax, wick, is_lit=False):
        self.__size = size
        self.__wax = wax
        self.__wick = wick
        self.__burn_time = self.calculate_burn_time()
        self.is_lit = is_lit

    def light(self):
        self.is_lit = True

    def extinguish(self):
        self.is_lit = False

    def calculate_burn_time(self):
        return round(
            self.__wax.get_burn_time() * self.__wick.get_burn_time(),
            2
        )

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if not self.is_lit:
            self.__size = size

    def __str__(self):
        return f"Candle size: {self.__size}, Burn time: {self.__burn_time}"

wax_1 = Wax("Paraffin")
wax_2 = Wax("Bee")
wax_3 = Wax("Soy")

wick_1 = Wick(4.0)
wick_2 = Wick(7.0)
wick_3 = Wick(8.0)

candle_1 = Candle("jar", wax_1, wick_1)
candle_2 = Candle("pillar", wax_2, wick_2)
candle_3 = Candle("large", wax_3, wick_3)

print(wax_1)
print(wick_1)
print(candle_1)

print(wax_2)
print(wick_2)
print(candle_2)

print(wax_3)
print(wick_3)
print(candle_3)