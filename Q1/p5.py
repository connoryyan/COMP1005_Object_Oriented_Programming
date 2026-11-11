class Tissue:
    def __init__(self, ply, scent, is_hypoallergenic):
        self.__ply = ply
        self.__scent = scent
        self.__is_hypoallergenic = is_hypoallergenic

    def get_ply(self):
        return self.__ply

    def set_ply(self, ply):
        if ply >= 1:
            self.__ply = ply

    def __str__(self):
        result = f"{self.__ply}-ply tissue, Scent: {self.__scent}"

        if self.__is_hypoallergenic:
            result += ", Hypoallergenic"

        return result


class TissueBox:
    def __init__(self, maximum_tissue_count=10):
        self.maximum_tissue_count = maximum_tissue_count
        self.__tissues = []

    def refill_maximum_tissues(self, tissue):
        if not isinstance(tissue, Tissue):
            return

        while len(self.__tissues) < self.maximum_tissue_count:
            self.__tissues.append(tissue)

    def refill_some_tissues(self, amount, tissue):
        if not isinstance(tissue, Tissue):
            return

        while (
            amount > 0
            and len(self.__tissues) < self.maximum_tissue_count
        ):
            self.__tissues.append(tissue)
            amount -= 1

    def take_single_tissue(self):
        if len(self.__tissues) == 0:
            print("The tissue box is empty.")
            return False

        self.__tissues.pop()
        print("You take a tissue.")
        return True

    def take_multiple_tissues(self, amount):
        if (not isinstance(amount, int) or isinstance(amount, bool)
                or amount <= 0 or amount > len(self.__tissues)):
            print("Invalid quantity or not enough tissues.")
            return False

        for _ in range(amount):
            self.__tissues.pop()

        print(f"You take {amount} tissues.")
        return True

    def __str__(self):
        if len(self.__tissues) == 0:
            return "The tissue box is empty and does not contain tissues."

        result = "Tissue box contains:\n"

        for tissue in self.__tissues:
            result += str(tissue) + "\n"

        return result.rstrip()


# Testing code

tissue_1 = Tissue(1, "Citrus", True)
tissue_2 = Tissue(5, "Lavender", False)
tissue_3 = Tissue(6, "Rose", False)

print(tissue_1)
print(tissue_2)
print(tissue_3)

tissue_box = TissueBox(9)

print(tissue_box)

update_1 = str(tissue_box)

# Add 4 tissue_1 tissues
tissue_box.refill_some_tissues(4, tissue_1)

# Add 3 tissue_2 tissues
tissue_box.refill_some_tissues(3, tissue_2)

# Fill the remaining 2 spaces with tissue_3
tissue_box.refill_maximum_tissues(tissue_3)

print(tissue_box)

update_2 = str(tissue_box)

# Take one tissue
tissue_box.take_single_tissue()

# Take two tissues
tissue_box.take_multiple_tissues(2)

print(tissue_box)

update_3 = str(tissue_box)
