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
    flowers_storage = []
    while True:
        flower = str(input())
        if flower == "":
            break

        flowers_storage.append(flower)

    print(bouquet_designs)
    print(flowers_storage)


if __name__ == '__main__':
    main()
