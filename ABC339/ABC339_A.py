def my_answer():
    S = input()
    charts = list(map(str, S.split('.')))
    charts_each_length= [len(charts[i]) for i in range(len(charts))]
    print(charts[-1])
    # print(charts_each_length)



if __name__ == '__main__':
    my_answer()