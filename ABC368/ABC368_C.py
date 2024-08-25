def calculate_min_turns(enemies):
    enemies.sort(reverse=True)
    total_turns = 0
    current_turn = 0
    remaining_enemies = len(enemies)

    while remaining_enemies > 0:
        current_turn += 1
        damage = 3 if current_turn % 3 == 0 else 1

        if enemies[remaining_enemies - 1] <= damage:
            remaining_enemies -= 1

        total_turns += 1

    return total_turns


def main():
    N = int(input())
    enemies = list(map(int, input().split()))
    result = calculate_min_turns(enemies)
    print(result)


if __name__ == "__main__":
    main()
