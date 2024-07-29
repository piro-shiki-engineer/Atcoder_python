def my_answer():
    N = int(input())

    sweet_dish_counter = 0
    dishes = [input() for _ in range(N)]
    for now_dish in dishes:
        if now_dish == 'sweet':
            if sweet_dish_counter < 2:
                sweet_dish_counter += 1
            else:
                print("No")
                exit()
        else:
            if sweet_dish_counter < 2:
                sweet_dish_counter = 0
            else:
                print("No")
                exit()
    print("Yes")


if __name__ == '__main__':
    my_answer()
