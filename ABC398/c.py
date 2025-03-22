from collections import defaultdict


def main():
    N = int(input())
    A_list = list(map(int, input().split()))

    unique_val_count = defaultdict(list)
    max_val_i = -1
    max_val = -1

    for i, val in enumerate(A_list):
        unique_val_count[val].append(i+1)

    for val, list_of_index in unique_val_count.items():
        if len(list_of_index) == 1 and max_val < val:
            max_val = max(max_val, val)
            max_val_i = list_of_index[0]

    print(max_val_i)

if __name__ == "__main__":
    main()
