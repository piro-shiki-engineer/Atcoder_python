import copy

def my_answer():
    N = int(input())
    Q_list = list(map(int, input().split()))
    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    max_A = 10**6
    max_B = 10**6
    max_males = 0

    for i in range(N):
        if A_list[i] > 0:
            max_A = min(max_A, Q_list[i]/A_list[i])
        if B_list[i] > 0:
            max_A = min(max_B, Q_list[i] / B_list[i])
    max_males = max(max_males(Q_list, A_list, B_list, max_A, N), max_males(Q_list, B_list, A_list, max_B, N))
    print(max_males)

def max_males(Q_list, prinmary_dish, another_dish, max_primary, N):
    max_males = 0
    for p in range(max_primary):
        remain = copy.copy(Q_list)
        for i in range(N):
            remain[i] -= prinmary_dish[i]*p
        secondMeals = int('inf')

        for i in range(N):
            if another_dish[i] > 0:
                secondMeals = min(secondMeals, remain[i]/another_dish[i])
        max_meals = max(max_males, p+secondMeals)
        return max_meals







if __name__ == "__main__":
    my_answer()
