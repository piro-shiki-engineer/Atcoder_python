
def my_answer():
    N, S, K = map(int, input().split())
    goods = []
    #送料
    pst = 0
    for i in range(N):
        P, Q = map(int, input().split())
        value = P*Q
        goods.append(value)

    total = sum(goods)
    if total >= S:
        pass
    else:
        total = total + K

    print(total)





if __name__ == '__main__':
    my_answer()