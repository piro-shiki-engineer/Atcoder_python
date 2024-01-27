def my_answer():
    chars = input()
    str_first = False
    str_other = False
    if chars[0].isupper():
        str_first = True

    if chars[1:].islower():
        str_other = True

    if str_first and str_other:
        print("Yes")
    elif len(chars) == 1 and str_first:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    my_answer()
