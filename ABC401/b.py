def main():
    N = int(input())
    auth_error_num = 0

    logged_in = False

    for _ in range(N):
        s_i = input()

        if s_i == "login":
            logged_in = True
        if s_i == "logout":
            logged_in = False

        if not logged_in:
            if s_i == "public":
                continue
            elif s_i == "private":
                auth_error_num += 1

    print(auth_error_num)


if __name__ == "__main__":
    main()
