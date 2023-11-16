def resolve():
    N = int(input())
    chars = list(input())
    myresult = bool
    index_numbers = []

    for val in range(0, len(chars)):
        if "a" == chars[val]:
            index_numbers.append(val)
    if not index_numbers == []:
        for index in index_numbers:
            if index == N - 1:
                if chars[index - 1] == "b":
                    myresult = True
                    break
            else:
                if chars[index - 1] == "b" or chars[index + 1] == "b":
                    myresult = True
                    break

    if myresult:
        print("Yes")

    else:
        print("No")
