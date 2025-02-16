def main():
    s1, s2 = map(str ,input().split())

    if s1 == "sick":
        if s2 == "sick":
            print("1")
        else:
            print("2")

    else: # s1 == "fine"
        if s2 == "sick":
            print("3")
        else:
            print("4")


if __name__ == '__main__':
    main()
