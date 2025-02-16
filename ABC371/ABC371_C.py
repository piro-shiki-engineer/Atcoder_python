def main():
    # 入力の読み取り
    # 頂点数 N
    N = int(input().strip())

    # グラフ G の辺の数 M_G
    M_G = int(input().strip())
    edges_G = []

    # グラフ G の辺の情報
    for _ in range(M_G):
        u, v = map(int, input().strip().split())
        edges_G.append((u - 1, v - 1))  # 0-based index にする

    # グラフ H の辺の数 M_H
    M_H = int(input().strip())
    edges_H = []

    # グラフ H の辺の情報
    for _ in range(M_H):
        a, b = map(int, input().strip().split())
        edges_H.append((a - 1, b - 1))  # 0-based index にする

    # コスト行列 A の読み取り
    cost = []
    for i in range(N - 1):
        row = list(map(int, input().strip().split()))
        cost.append(row)

    # 隣接行列でグラフを表現する関数
    def create_adjacency_matrix(N, edges):
        adj_matrix = [[0] * N for _ in range(N)]
        for u, v in edges:
            adj_matrix[u][v] = 1
            adj_matrix[v][u] = 1
        return adj_matrix

    # G, H の隣接行列を作成
    adj_G = create_adjacency_matrix(N, edges_G)
    adj_H = create_adjacency_matrix(N, edges_H)

    # エッジの状態をビット列で表現
    def graph_to_bitmask(adj_matrix):
        bitmask = 0
        bit_position = 0
        for i in range(N):
            for j in range(i + 1, N):
                if adj_matrix[i][j] == 1:
                    bitmask |= (1 << bit_position)
                bit_position += 1
        return bitmask

    target_mask = graph_to_bitmask(adj_G)
    initial_mask = graph_to_bitmask(adj_H)

    # 状態の全数
    MAX_STATE = 1 << (N * (N - 1) // 2)

    # DPテーブル
    dp = [float('inf')] * MAX_STATE
    dp[initial_mask] = 0

    # エッジの位置インデックスの取得
    def get_edge_index(i, j):
        # (i, j) のビット位置を計算
        return i * (N - 1) - i * (i + 1) // 2 + j - i - 1

    # グラフを同型にするための最小コスト計算
    for state in range(MAX_STATE):
        if dp[state] == float('inf'):
            continue

        # 現在の状態でのグラフ構築
        bit_position = 0
        for i in range(N):
            for j in range(i + 1, N):
                edge_index = get_edge_index(i, j)
                # エッジの状態のトグル
                if (state & (1 << edge_index)) == 0:  # エッジが存在しない場合
                    new_state = state | (1 << edge_index)
                    dp[new_state] = min(dp[new_state], dp[state] + cost[i][j - i - 1])
                else:  # エッジが存在する場合
                    new_state = state & ~(1 << edge_index)
                    dp[new_state] = min(dp[new_state], dp[state] + cost[i][j - i - 1])

    # 結果の出力
    print(dp[target_mask])


if __name__ == "__main__":
    main()