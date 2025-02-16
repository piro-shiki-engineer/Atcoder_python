def main():
    S_AB, S_AC, S_BC = map(str, input().split())

    if S_AB == '<' and S_AC == '<' and S_BC == '<':
        order = ['A', 'B', 'C']
    elif S_AB == '<' and S_AC == '<' and S_BC == '>':
        order = ['A', 'C', 'B']
    elif S_AB == '<' and S_AC == '>' and S_BC == '>':
        order = ['C', 'A', 'B']
    elif S_AB == '>' and S_AC == '>' and S_BC == '>':
        order = ['C', 'B', 'A']
    elif S_AB == '>' and S_AC == '>' and S_BC == '<':
        order = ['B', 'C', 'A']
    elif S_AB == '>' and S_AC == '<' and S_BC == '<':
        order = ['B', 'A', 'C']

    print(order[1])


if __name__ == '__main__':
    main()
