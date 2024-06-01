def find_criminal(A, B):
    # 全ての候補者
    candidates = {1, 2, 3}

    candidates.discard(A)
    candidates.discard(B)

    if len(candidates) == 1:
        return candidates.pop()
    else:
        return -1


if __name__ == '__main__':
    A, B = map(int, input().split())
    print(find_criminal(A, B))
