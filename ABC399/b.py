def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0)

    participants = [[i, P[i]] for i in range(1, N + 1)]
    participants.sort(key=lambda x: x[1], reverse=True)

    rank = 1
    ranks = [0] * (N + 1)

    i = 0
    while i < N:
        current_score = participants[i][1]
        same_score_count = 0

        while (
            i + same_score_count < N
            and participants[i + same_score_count][1] == current_score
        ):
            participant_id = participants[i + same_score_count][0]
            ranks[participant_id] = rank
            same_score_count += 1

        rank += same_score_count
        i += same_score_count

    for i in range(1, N + 1):
        print(ranks[i])


if __name__ == "__main__":
    main()
