def my_answer():
    correct = input()
    correct_index = []
    wrong = input()
    i = 0

    for s_char in correct:
        while i < len(wrong):
            if wrong[i] == s_char:
                correct_index.append(str(i + 1))  # 人間が読むインデックスに合わせるために+1する
                i += 1  # 次の位置から探し始める
                break
            i += 1

    print(' '.join(correct_index))


if __name__ == '__main__':
    my_answer()