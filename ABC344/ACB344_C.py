def my_answer():
    N = int(input())
    A_list = list(map(int, input().split()))
    M = int(input())
    B_list = list(map(int, input().split()))
    L = int(input())
    C_list = list(map(int, input().split()))
    Q = int(input())
    X_list = list(map(int, input().split()))

    # AとBから選んだ数の和の全ての可能性を計算し、セットに格納
    AB_sums = set(a + b for a in A_list for b in B_list)

    for x in X_list:
        # Cから選んだ数がAB_sumsの補完として存在するかをチェック
        if any(x - c in AB_sums for c in C_list):
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    my_answer()
