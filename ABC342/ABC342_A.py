def my_answer():
    S = input()

    # 最初の3文字を確認して、多数決の原理を適用
    if S[0] == S[1] or S[0] == S[2]:
        majority = S[0]
    else:
        majority = S[1]

    # 多数を占める文字と異なる文字を探す
    for i in range(len(S)):
        if S[i] != majority:
            print(i + 1)
            return


if __name__ == '__main__':
    my_answer()
