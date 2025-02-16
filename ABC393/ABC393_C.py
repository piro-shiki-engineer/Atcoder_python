def main():
    n, m = map(int, input().split())
    edges = {}
    result = 0

    for i in range(m):
        u_i, v_i = map(int, input().split())
        u_i, v_i = u_i-1, v_i-1
        if edges.get((u_i, v_i), False) or u_i == v_i:
            result += 1
        else:
            edges[(u_i, v_i)] = True
            edges[(v_i, u_i)] = True
    print(result)


if __name__ == '__main__':
    main()
