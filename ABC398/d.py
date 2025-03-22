def move_reverse(x: str):
    if x == "N":
        return 1, 0  # 北風の逆方向は南
    elif x == "W":
        return 0, 1  # 西風の逆方向は東
    elif x == "S":
        return -1, 0  # 南風の逆方向は北
    elif x == "E":
        return 0, -1  # 東風の逆方向は西
    return 0, 0


def main():
    N, R, C = map(int, input().split())
    S = input()

    # 煙の位置の集合
    smoke_positions = {(0, 0)}  # 最初の煙は原点に

    # 焚き火と高橋君の位置
    fire_r, fire_c = 0, 0
    takahashi_r, takahashi_c = R, C

    results = []

    for t in range(1, N + 1):
        # 焚き火と高橋君を風の逆方向に移動
        dr, dc = move_reverse(S[t - 1])
        fire_r += dr
        fire_c += dc
        takahashi_r += dr
        takahashi_c += dc

        # 現在の焚き火位置に煙を生成
        smoke_positions.add((fire_r, fire_c))

        # 高橋君の位置に煙があるかチェック
        has_smoke = (takahashi_r, takahashi_c) in smoke_positions
        results.append("1" if has_smoke else "0")

    print("".join(results))


if __name__ == "__main__":
    main()
