def main():
    def color_depend_on_num(number: int) -> str:
        if number % 2 == 0:
            return "#"
        return "."

    N = int(input())
    grid = [["?" for  _ in range(N)]  for  _ in range(N)]

    for i in range(N//2+1):
        j = N + 1 - i - 1
        color = color_depend_on_num(i)
        for dx in range(j-i):
            for dy in range(j-i):
                grid[i + dx][i + dy] = color

    for i in range(N):
        print("".join(grid[i]))


if __name__ == '__main__':
    main()