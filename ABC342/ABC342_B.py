def my_answer():
    N = int(input())
    people = list(map(int, input().split()))
    Q = int(input())
    query_list = [list(map(int, input().split())) for _ in range(Q)]
    # print(people)
    # print()
    for i in range(Q):
        A_i, B_i = query_list[i][0], query_list[i][1]
        # print("q:", A_i, B_i)
        person_num_A = people.index(A_i) + 1
        person_num_B = people.index(B_i) + 1
        if person_num_A < person_num_B:
            print(A_i)
        else:
            print(B_i)

if __name__ == '__main__':
    my_answer()
