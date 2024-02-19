def my_answer():
    N = int(input())
    cash_per_country = list(map(int, input().split()))
    action_per_country = {i: {'s_i': 0, 't_i': 0} for i in range(N-1)}
    for i in range(N-1):
        s_i, t_i = map(int, input().split())
        action_per_country[i]['s_i'] = s_i
        action_per_country[i]['t_i'] = t_i

    ans = 0
    tmp = 0
    exchange_next_country_cash = 0
    for i in range(N-1):
        country = i
        exchange_to_next = int(cash_per_country[i]/action_per_country[i]['s_i'])
        cash_per_country[i+1] += exchange_to_next * action_per_country[i]['t_i']

    print(cash_per_country[-1])


if __name__ == '__main__':
    my_answer()
