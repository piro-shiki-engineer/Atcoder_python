def my_answer():
    N = int(input())
    card_list = []
    remain_card = []

    for i in range(N):
        strong, cost = map(int, input().split())
        card_list.append([i+1, strong, cost])
    print(card_list)
    card_list.sort(key= lambda x: x[1])
    print(card_list)

    min_cost = float('inf')

    for i in range(N-1, -1, -1):
        index, strong, cost = map(int, card_list[i])
        if cost < min_cost:
            remain_card.append(index)
            min_cost = cost

    print(remain_card.sort())


if __name__ == '__main__':
    my_answer()
