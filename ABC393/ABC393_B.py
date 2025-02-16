def main():
    s = "0" + input()
    n = len(s)
    result = 0
    for i in range(1, n):
        max_interval  = (n-i) // 2

        for interval in range(1, max_interval+1):
            j = i + interval
            k = j + interval
            if k < n and s[i] == 'A' and s[j] == 'B' and s[k] == 'C':
                result += 1
    print(result)


if __name__ == '__main__':
    main()
