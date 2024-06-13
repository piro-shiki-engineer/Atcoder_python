def my_answer():
    N, M = map(int, input().split())

    objective_nutrition = list(map(int, input().split()))
    intake_nutrition = [0]*M
    check_enough = [False]*M
    for i in range(N):
        nutrition_per_dish = list(map(int, input().split()))
        for j in range(M):
            intake_nutrition[j] += nutrition_per_dish[j]

    for i in range(M):
        check_enough[i] = intake_nutrition[i] >= objective_nutrition[i]

    if all(check_enough):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    my_answer()
