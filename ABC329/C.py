import itertools
import collections


def my_answer():
    n = int(input())
    s = input()

    # 連続したアルファベットを記録、初期値は0
    d = collections.defaultdict(int)

    for c, g in itertools.groupby(s):
        d[c] = max(d[c], len(list(g)))

    print(sum(d.values()))


if __name__ == '__main__':
    my_answer()
