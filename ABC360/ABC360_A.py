def my_answer():
    S = input()
    dish_index = {S[i]: i for i in range(len(S))}

    if dish_index['R'] < dish_index['M']:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    my_answer()
