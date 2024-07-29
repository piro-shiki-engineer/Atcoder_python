def my_answer():
    N, X, Y = map(int, input().split())
    sweet_dishes = list(map(int, input().split()))
    salty_dishes = list(map(int, input().split()))
    dish_numbers = [i for i in range(N)]

    dishes = [(sweet_dishes[i], salty_dishes[i]) for i in range(N)]
    dishes.sort(key=lambda x: (x[0] + x[1]))

    sweet_sum = 0
    salty_sum = 0
    min_dishes = 0

    for sweet, salty in dishes:
        sweet_sum += sweet
        salty_sum += salty
        min_dishes += 1

        if sweet_sum > X or salty_sum > Y:
            break

    print(min_dishes)


if __name__ == '__main__':
    my_answer()
