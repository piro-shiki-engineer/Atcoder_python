def my_answer():
    N, M = map(int, input().split())

    friends_each_person = {i:[] for i in range(1, N+1)}

    for _ in range(M):
        relation = list(map(int, input().split()))
        friends_each_person[relation[0]].append(relation[1])
        friends_each_person[relation[1]].append(relation[0])

    print(friends_each_person)