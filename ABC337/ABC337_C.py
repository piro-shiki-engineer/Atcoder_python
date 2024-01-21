
def get_key_from_value(d, val):
    keys = [k for k, v in d.items() if v == val]
    if keys:
        return keys[0]
    return None


def my_answer():
    N = int(input())
    persons = list(map(int, input().split()))
    answer = []

    persons_mapping = {person_num+1: persons[person_num] for person_num in range(N)}
    first_person = min(persons_mapping, key=persons_mapping.get)
    # print(persons)
    # print(persons_mapping)
    # print("先頭", first_person)

    answer.append(first_person)
    next_person = get_key_from_value(persons_mapping, first_person)
    # print(next_person)

    for _ in range(1, len(persons)):
        answer.append(next_person)
        next_person = get_key_from_value(persons_mapping, next_person)

    for i in answer:
        print(i, end=" ")


    # 3 5 4 1 2 6


if __name__ == '__main__':
    my_answer()
