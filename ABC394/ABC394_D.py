def main():
    S = input()
    if len(S) % 2 != 0:
        print("No")
        return

    current_str = S
    brackets = {
        ')': '(',
        ']': '[',
        '>': '<'
    }

    while True:
        stack = []
        i = 0
        changed = False

        while i < len(current_str):
            if len(stack) > 0 and i < len(current_str) and \
                    current_str[i] in brackets and brackets[current_str[i]] == stack[-1]:
                stack.pop()
                changed = True
            else:
                stack.append(current_str[i])
            i += 1

        current_str = ''.join(stack)

        if not changed:
            break

    print("Yes" if len(current_str) == 0 else "No")


if __name__ == '__main__':
    main()