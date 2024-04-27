def my_answer():
    N = int(input())
    A = list(map(int, input().split()))

    swaps = []
    index_map = {value: i for i, value in enumerate(A)}

    for i in range(N):
        while A[i] != i + 1:
            swap_with_idx = index_map[i + 1]
            # Record the swap operation
            swaps.append((i + 1, swap_with_idx + 1))

            # Swap the elements in the array
            A[i], A[swap_with_idx] = A[swap_with_idx], A[i]

            # Update the index_map
            index_map[A[i]], index_map[A[swap_with_idx]] = i, swap_with_idx

    print(len(swaps))

    for swap in swaps:
        print("{} {}".format(swap[0], swap[1]))


if __name__ == '__main__':
    my_answer()