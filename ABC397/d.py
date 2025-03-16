def main():
    N = int(input())
    # Nの約数dをすべて試す
    d = 1
    while d * d <= N:
        if N % d == 0:
            # dが有効かチェック
            k = N // d
            discriminant = 12 * k - 3 * d * d
            if discriminant < 0:
                d += 1
                continue

            sqrt_discriminant = int(discriminant ** 0.5)
            if sqrt_discriminant ** 2 == discriminant:  # 完全平方数
                # yの2つの可能な値
                y1 = (-3 * d + sqrt_discriminant) // 6
                y2 = (-3 * d - sqrt_discriminant) // 6

                if y1 > 0 and (-3 * d + sqrt_discriminant) % 6 == 0:
                    print(f'{y1 + d} {y1}')
                    exit()
                if y2 > 0 and (-3 * d - sqrt_discriminant) % 6 == 0:
                    print(f'{y2 + d} {y2}')
                    exit()

            # N/dがdとして機能するかチェック
            large_d = N // d
            k_large = N // large_d
            discriminant_large = 12 * k_large - 3 * large_d * large_d

            if discriminant_large >= 0:
                sqrt_discriminant_large = int(discriminant_large ** 0.5)
                if sqrt_discriminant_large * sqrt_discriminant_large == discriminant_large:
                    y1 = (-3 * large_d + sqrt_discriminant_large) // 6
                    y2 = (-3 * large_d - sqrt_discriminant_large) // 6

                    if y1 > 0 and (-3 * large_d + sqrt_discriminant_large) % 6 == 0:
                        print(f'{y1 + large_d} {y1}')
                        exit()
                    if y2 > 0 and (-3 * large_d - sqrt_discriminant_large) % 6 == 0:
                        print(f'{y2 + large_d} {y2}')
                        exit()

        d += 1

    print('-1 -1')


if __name__ == '__main__':
    main()
