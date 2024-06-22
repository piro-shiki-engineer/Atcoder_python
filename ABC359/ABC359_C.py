def my_answer():
    s_x, s_y = map(int, input().split())
    t_x, t_y = map(int, input().split())

    s_x -= (s_x + s_y) % 2
    t_x -= (t_x + t_y) % 2

    # スタートを原点に並行移動
    t_x -= s_x
    t_y -= s_y

    # 目的地を第1象限に移動
    t_x = abs(t_x)
    t_y = abs(t_y)

    print(t_y + max(0, (t_x - t_y) // 2))


if __name__ == '__main__':
    my_answer()
