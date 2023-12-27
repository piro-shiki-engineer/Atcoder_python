def min_oddness_pairs(N, K, lost_colors):
    # 靴下の色ごとのカウントを初期化（全ての色で2枚ずつ存在）
    sock_counts = [2] * N

    # 失われた靴下の色を1減らす
    for color in lost_colors:
        sock_counts[color - 1] -= 1

    # 奇妙さの総和を計算
    oddness_sum = 0
    remaining_socks = 0

    for count in sock_counts:
        # 奇数の場合、最も近い色とペアにする
        if remaining_socks > 0 and count > 0:
            oddness_sum += 1  # 最も近い色なので奇妙さは1
            remaining_socks -= 1  # 余りを1減らす
            count -= 1  # この色の靴下を1減らす

        # 同じ色のペアを作る
        pairs = count // 2
        remaining_socks += count % 2  # 余りを加算

    return oddness_sum

def my_answer():
    N, K = map(int, input().split())
    lost_colors = list(map(int, input().split()))

    # 奇妙さの総和を計算
    result = min_oddness_pairs(N, K, lost_colors)
    print(result)


if __name__ == "__main__":
    my_answer()
