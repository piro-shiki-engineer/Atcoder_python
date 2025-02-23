def main():
    s = input()
    n = len(s)
    s_list = list(s)

    i = 0
    while i < n-1:
        if s_list[i] == "W" and s_list[i+1] == "A":
            s_list[i] = "A"
            s_list[i+1]  = "C"
            if i > 0:
                i -= 1
            else:
                i +=1
        else:
            i += 1

    print("".join(s_list))


if __name__ == '__main__':
    main()