def my_answer():
    A, B, C = map(int, input().split())
    val = A**2 + B**2

    if val < C**2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    my_answer()
