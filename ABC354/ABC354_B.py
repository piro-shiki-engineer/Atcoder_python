def my_answer():
    N = int(input())
    user_list = []
    total_rate = 0

    for _ in range(N):
        user_name, rate = map(str, input().split())
        rate = int(rate)

        user_list.append(user_name)
        total_rate += rate

    winner_index = total_rate % N
    user_list = sorted(user_list)
    print(user_list[winner_index])


if __name__ == '__main__':
    my_answer()
