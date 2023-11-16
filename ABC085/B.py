
def my_answer():
    N = int(input())
    count = set()
    for _ in range(N):
        count.add(int(input()))

    print(len(count))


if __name__ == '__main__':
    my_answer()
