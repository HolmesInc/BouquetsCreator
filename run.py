from collections import defaultdict


class FlowersStorage:
    def __init__(self):
        self.L = defaultdict(int)
        self.S = defaultdict(int)

    def append(self, flower: str):
        flower_size = flower[1]
        flower_specie = flower[0]
        getattr(self, flower_size)[flower_specie] += 1

    def is_amount_available(self, size: str, specie: str, amount: int):
        if amount <= getattr(self, size)[specie]:
            return True

        return False

    def reduce_amount(self, size: str, specie: str, amount: int):
        new_amount = getattr(self, size)[specie] - amount
        if new_amount < 0:
            raise ValueError("Amount of available flowers can't be less than 0")
        elif new_amount == 0:
            del getattr(self, size)[specie]
        else:
            getattr(self, size)[specie] = new_amount


class BouquetDesign:
    def __init__(self, design):
        self.design = design
        self.bouquet_name = design[0]
        self.bouquet_size = design[1]
        self.total_flowers_in_bouquet = BouquetDesign.get_total_flowers_in_bouquet(design)
        self.flowers = BouquetDesign.get_flowers(design[2:len(design) - len(str(self.total_flowers_in_bouquet))])

    @staticmethod
    def get_flowers(flowers_quantity_string: str):
        flowers = {}

        def _get_flower_species(bouquet_item: str):
            return bouquet_item.isalpha()

        flower_species = [*filter(_get_flower_species, flowers_quantity_string)]
        for flower_specie in flower_species:
            flowers[flower_specie], flowers_quantity_string = flowers_quantity_string.split(flower_specie)
            flowers[flower_specie] = int(flowers[flower_specie])

        return flowers

    @staticmethod
    def get_total_flowers_in_bouquet(bouquet_design: str):
        total_quantity = ''
        for index in range(len(bouquet_design) - 1, 0, -1):
            if bouquet_design[index].isnumeric():
                total_quantity = f"{bouquet_design[index]}{total_quantity}"
            else:
                break
        return int(total_quantity)


def main():
    """ Main function, perform action once script runs
    """
    bouquet_designs = []

    print('Please, enter bouquet designs. Once you finish, enter blank line for proceeding to the next step')
    while True:
        design = str(input())
        if design == "":
            break
        bouquet_designs.append(BouquetDesign(design))

    print('Please, enter flowers. Once you finish, enter blank line for proceeding to the next step')
    flowers_storage = FlowersStorage()
    while True:
        flower = input()
        if flower == "":
            break

        flowers_storage.append(flower)

    print(bouquet_designs)
    print(flowers_storage)


if __name__ == '__main__':
    main()
