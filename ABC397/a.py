def main():
    body_temp = float(input())
    if body_temp < 37.5:
        print(3)
    else:
        if body_temp < 38.0:
            print(2)
        else:
            print(1)


if __name__ == '__main__':
    main()