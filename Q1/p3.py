import random


class Lure:
    def __init__(self, type, description):
        self.__type = type
        self.__description = description

    def __str__(self):
        return f"Lure type: {self.__type}, Description: {self.__description}"

    def get_type(self):
        return self.__type

    def get_description(self):
        return self.__description


class FishingRod:
    def __init__(self, type, durability=100, lure=None):
        self.__type = type
        self.__durability = durability
        self.lure = lure

        # Make sure the initial durability is also clamped
        self.set_durability(durability)

    def get_durability(self):
        return self.__durability

    def set_durability(self, durability):
        if durability < 0:
            self.__durability = 0
        elif durability > 100:
            self.__durability = 100
        else:
            self.__durability = durability

    def cast(self):
        # Check whether the rod is already broken
        if self.__durability <= 0:
            print("The fishing rod is broken.")
            return False

        # Reduce durability by a random integer from 0 to 10
        damage = random.randint(0, 10)
        self.set_durability(self.__durability - damage)

        # Check whether a lure is attached
        if self.lure is None:
            print("There is no lure attached to the fishing rod.")
            return False

        print("The line was thrown.")
        return True

    def check_requires_repair(self):
        if self.__durability <= 0:
            print("The fishing rod is broken.")
            return True

        return False

    def repair_rod(self):
        self.set_durability(100)

    def check_durability(self):
        if self.__durability <= 25:
            return "is damaged"
        elif self.__durability <= 50:
            return "is in okay condition"
        elif self.__durability <= 75:
            return "is in great condition"
        else:
            return "is in excellent condition"

    def attach_lure(self, lure):
        if isinstance(lure, Lure):
            self.lure = lure

    def __str__(self):
        result = (
            f"A {self.__type} rod which {self.check_durability()}.\n"
        )

        if self.lure is None:
            result += "It doesn't have a lure attached."
        else:
            result += (
                f"It has a {self.lure.get_type()} lure attached: "
            )

        return result


# Testing code

lure_1 = Lure(
    "Spinner",
    "It attracts curious fish"
)

fishing_rod_1 = FishingRod("Fibreglass")

# First cast without a lure
fishing_rod_1.cast()

# Attach lure_1 and cast again
fishing_rod_1.attach_lure(lure_1)
fishing_rod_1.cast()

# Save snapshot
update_1 = str(fishing_rod_1)


lure_2 = Lure(
    "Sparkly",
    "It spins to attract fish"
)

fishing_rod_2 = FishingRod(
    "Wooden",
    durability=0
)

# Save initial snapshot
update_2 = str(fishing_rod_2)

# Attach lure_2 and try casting while broken
fishing_rod_2.attach_lure(lure_2)
fishing_rod_2.cast()

# Save snapshot
update_3 = str(fishing_rod_2)


# Display the results
print(update_1)
print(update_2)
print(update_3)


# Demonstrate repair
fishing_rod_2.repair_rod()
print(fishing_rod_2)

fishing_rod_2.cast()
