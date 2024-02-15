def my_answer():
    N, S, D = map(int, input().split())
    magic_list = [list(map(int, input().split())) for _ in range(N)]
    damage_flag = False

    for magic in magic_list:
        time, damage = magic[0], magic[1]
        if time >= S or damage <= D:
            continue
        damage_flag = True

        if damage_flag:
            print("Yes")
            exit()

    print("No")


if __name__ == '__main__':
    my_answer()
