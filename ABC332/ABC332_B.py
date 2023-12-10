
def my_answer():
    K, G, M = map(int, input().split())
    G_vol = 0
    M_vol = 0

    for i in range(K):
        if G_vol == G:
           G_vol = 0
        elif M_vol == 0:
            M_vol = M
        else:
            transfer = min(M_vol, G - G_vol)
            G_vol += transfer
            M_vol -= transfer
            # if M_vol <= G:
            #     G_vol = M_vol
            #     M_vol = 0
            # else:
            #     G_vol = G
            #     M_vol = M_vol - G

    print('{} {}'.format(G_vol, M_vol))


if __name__ == '__main__':
    my_answer()
