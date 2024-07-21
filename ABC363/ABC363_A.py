def my_answer():
    rate = int(input())
    rate_rank = "^" * ((rate // 100)+1)

    rate_diff = len(rate_rank)*100 - rate
    print(rate_diff)


if __name__ == '__main__':
    my_answer()
