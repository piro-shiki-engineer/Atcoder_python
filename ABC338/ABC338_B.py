def my_answer():
    chars = input()
    chars = [chars[i] for i in range(len(chars))]

    num_highest = 0
    num_friq = int
    possible = []
    ans = ''

    for char in chars:
        num_friq = chars.count(char)
        if num_friq > num_highest:
            num_highest = num_friq
            possible = list
            possible.append(char)

        elif num_friq == num_highest:
            possible.append(char)

    print(ans)

def find_most_common_letter():
    # Count the frequency of each letter in the string
    s = input()
    letter_counts = {}
    for letter in s:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    # Find the letter(s) with the highest frequency
    max_count = max(letter_counts.values())
    most_common_letters = [letter for letter, count in letter_counts.items() if count == max_count]
    print(min(most_common_letters))

    # Return the alphabetically first letter among the most common ones
    return min(most_common_letters)





if __name__ == "__main__":
    find_most_common_letter()