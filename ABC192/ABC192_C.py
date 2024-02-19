def sort_digit_bigger(a_i) -> int:
    digit_str = str(a_i)
    digit_list = []
    dig_str_list = []
    converted_digit = str
    for i in range(len(digit_str)):
        digit_list.append(int(digit_str[i]))
    digit_list.sort(reverse=True)
    for i in range(len(digit_str)):
        dig_str_list.append(str(digit_list[i]))
    converted_digit = ''.join(dig_str_list)

    return int(converted_digit)

def sort_digit_smaller(a_i) -> int:
    digit_str = str(a_i)
    digit_list = []
    dig_str_list = []
    converted_digit = str
    if int(digit_str) == 0 or len(digit_list) == 1:
        return a_i

    for i in range(len(digit_str)):
        digit_list.append(int(digit_str[i]))
    digit_list.sort()
    for i in range(len(digit_list)):
        dig_str_list.append(str(digit_list[i]))
    converted_digit = ''.join(dig_str_list)
    converted_digit = ''.join(dig_str_list)

    return int(converted_digit)

def next_a(a_i:int) -> int:
    return sort_digit_bigger(a_i) - sort_digit_smaller(a_i)

def my_answer():
    N, K = map(int, input().split())
    a_i = N
    for i in range(K):
        a_i = next_a(a_i)

    print(a_i)


if __name__ == '__main__':
    my_answer()
