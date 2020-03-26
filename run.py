def main():
    """ Main function, perform action once script runs
    """
    bouquet_designs = []

    print('Please, enter bouquet designs. Once you finish, enter blank line for proceeding to the next step')
    while True:
        design = str(input())
        if design == "":
            break
        bouquet_designs.append(design)

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
