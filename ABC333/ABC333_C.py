def generate_repunit(n:int):
    return (10**n - 1) // 9

def my_answer():
    N = int(input())
    repunits = []
    n = 1

    while len(repunits) < N:
        repunit = generate_repunit(n)
        for i in range(n):
            for j in range(i, n):
                repunits.append(repunit)
        n += 1

    repunit_sums = sorted(set(x + y + z for x in repunits for y in repunits for z in repunits))[:N]

    print(repunit_sums[N-1])




if __name__ == "__main__":
    my_answer()
