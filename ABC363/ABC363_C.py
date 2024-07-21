def next_permutation(seq):
    i = len(seq) - 2
    while i >= 0 and seq[i] >= seq[i + 1]:
        i -= 1
    if i == -1:
        return False

    j = len(seq) - 1
    while seq[j] <= seq[i]:
        j -= 1

    seq[i], seq[j] = seq[j], seq[i]

    seq[i + 1:] = reversed(seq[i + 1:])
    return True


def is_palindrome(s):
    return s == s[::-1]


def count_non_palindromic_permutations(N, K, S):
    s_list = sorted(S)
    palindrome_memo = {}
    ans = 0

    while True:
        pattern = ''.join(s_list)
        substring_flag = False
        for i in range(N - K + 1):
            sub_pattern = pattern[i:i + K]
            if sub_pattern in palindrome_memo:
                if palindrome_memo[sub_pattern]:
                    substring_flag = True
                    break
            else:
                is_pal = is_palindrome(sub_pattern)
                palindrome_memo[sub_pattern] = is_pal
                if is_pal:
                    substring_flag = True
                    break
        if not substring_flag:
            ans += 1

        if not next_permutation(s_list):
            break

    return ans


def my_answer():
    N, K = map(int, input().split())
    S = input().strip()
    answer = count_non_palindromic_permutations(N, K, S)
    print(answer)


if __name__ == '__main__':
    my_answer()
