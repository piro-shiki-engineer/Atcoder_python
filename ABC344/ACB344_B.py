def my_answer():
    A_list = []
    flag = True
    while flag:
        input_val = int(input())
        if input_val == 0:
            A_list.append(input_val)
            flag = False
        else:
            A_list.append(input_val)

    for i in range(len(A_list)):
        print(A_list[-(i+1)])


if __name__ == '__main__':
    my_answer()
