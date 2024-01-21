def my_answer():
    N = int(input())

    total_x = total_y = 0

    for _ in range(N):
        X_i, Y_i = map(int, input().split())
        total_x += X_i
        total_y += Y_i

    if total_x > total_y:
        print("Takahashi")
    elif total_x < total_y:
        print("Aoki")
    else:
        print("Draw")

if __name__ == "__main__":
    my_answer()
