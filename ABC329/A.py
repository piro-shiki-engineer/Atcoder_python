def my_answer():
    chars = input()
    answer = str()

    if chars[1] == ' ':
        chars = [char for char in chars if char != ' ']
    else:
        chars = [str(chars[i] + ' ') for i in range(len(chars))]

    for char in chars:
        answer += str(char)

    print(answer)

if __name__ == '__main__':
    my_answer()
