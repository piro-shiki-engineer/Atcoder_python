def main():
    n, m = map(int, input().split())
    matrix = [[False]*n for _ in range(n)]
    result = 0

    for i in range(m):
        u_i, v_i = map(int, input().split())
        u_i, v_i = u_i-1, v_i-1
        if matrix[u_i][v_i] == True or u_i == v_i:
            result += 1
        else:
            matrix[u_i][v_i] = True
            matrix[v_i][u_i] = True

    print(result)

if __name__ == '__main__':
    main()
