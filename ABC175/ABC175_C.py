def my_answer():
    X, K, D = map(int, input().split())
    X = abs(X)

    if X - K*D > 0:
        print(X-(K*D))
    else:
        move_count = K - (X//D)
        jump_before = X - D*(X//D)
        jump_after = jump_before - D
        if move_count % 2 == 0:
            print(abs(jump_before))
        else:
            print(abs(jump_after))


if __name__ == '__main__':
    my_answer()
