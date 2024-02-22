import math

def my_answer():
    N, X = map(int, input().split())
    total_alcohol = 0
    alcohol_list = []
    for i in range(N):
        alcohol = list(map(int, input().split()))
        alcohol_list.append(alcohol)

    for i in range(N):
        total_alcohol += alcohol_list[i][0] * alcohol_list[i][1]
        #print(get_alcohol)

        if total_alcohol > X*100:
            print(i+1)
            exit()

    print(-1)


if __name__ == '__main__':
    my_answer()
