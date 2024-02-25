def my_answer():
    N = int(input())
    S = input()
    Q = int(input())
    query_list = [list(map(str, input().split())) for _ in range(Q)]

    # 置換を追跡するための辞書
    replace_dict = {chr(ord('a') + i): chr(ord('a') + i) for i in range(26)}

    # クエリを処理して置換ルールを更新
    for c_i, d_i in query_list:
        for key, value in replace_dict.items():
            if value == c_i:
                replace_dict[key] = d_i

    # 置換ルールに基づいて文字列を組み立て直す
    result = ''.join(replace_dict[char] for char in S)

    print(result)


if __name__ == '__main__':
    my_answer()
