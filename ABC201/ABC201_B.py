def my_answer():
    N = int(input())
    mountains = {}
    mountain_heights = []
    for _ in range(N):
        s, t = map(str, input().split())
        t = int(t)
        mountain_heights.append(t)
        mountains[t] = s

    mountain_heights.sort()
    print(mountains[mountain_heights[-2]])


def another_answer():
    N = int(input())

    mountains = []

    for i in range(N):
        S, T = map(str, input().split())
        T = int(T)
        mountains.append([T, S])

    mountains.sort(reverse=True)
    print(mountains[1][1])


if __name__ == '__main__':
    my_answer()
