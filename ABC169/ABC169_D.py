def prime_factorize(N: int) -> list:
    if N == 1:
        return [1]
    prime_list= []
    i=2
    while i*i <= N:
        if N % i == 0:
            prime_list.append(i)
            N //= i
        else:
            i += 1
    if N != 1:
        prime_list.append(N)
    return prime_list


def my_answer():
    N = int(input())

    if N == 1:
        print(0)
        exit()

    prime_N = prime_factorize(N)
    prime_N = set(prime_N)

    ans = 0

    for p in prime_N:
        for e in range(1, 10**10):
            if N % (p**e) == 0:
                ans += 1
                N //= p**e
            else:
                break

    print(ans)


if __name__ == '__main__':
    my_answer()

