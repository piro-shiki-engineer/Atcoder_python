import math

def calculate_ceil(X):
    # If X is divisible by 10, just return X // 10
    if X % 10 == 0:
        return X // 10
    # If X is positive and not divisible by 10, add 1 to the integer division result
    elif X > 0:
        return X // 10 + 1
    # For negative numbers, if X is not divisible by 10, we should return X // 10 (not subtracting 1)
    else:
        return (X // 10) if X % 10 == 0 else (X // 10) + 1


def my_answer():
    X = int(input())
    result = calculate_ceil(X)
    print(result)


if __name__ == '__main__':
    my_answer()
