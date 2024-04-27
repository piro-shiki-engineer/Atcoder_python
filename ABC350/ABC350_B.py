def my_answer():
    N, Q = map(int, input().split())
    surgery_list = list(map(int, input().split()))

    teeth_status = [True for i in range(N)]
    total = len(teeth_status)
    for teeth_num in surgery_list:
        if teeth_status[teeth_num-1] == True:
            teeth_status[teeth_num-1] = False
            total -= 1
        else:
            teeth_status[teeth_num-1] = True
            total += 1
    print(total)


if __name__ == '__main__':
    my_answer()