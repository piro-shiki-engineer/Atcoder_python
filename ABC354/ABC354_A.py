def my_answer():
    height = int(input())
    plant_height = 1
    i = 1

    while plant_height <= height:
        plant_height += (2**i)
        i += 1
    print(i)


if __name__ == '__main__':
    my_answer()
