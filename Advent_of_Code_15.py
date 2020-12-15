
# starting_numbers = [0, 3, 6]
starting_numbers = [0, 13, 1, 8, 6, 15]


def memory_game(starting_nums: list) -> list:
    numbers_dict = {}
    all_spoken = []
    for i in range(1, 2021):
        # starting number
        if i <= len(starting_nums):
            said_number = starting_numbers[i-1]
            all_spoken.append(said_number)
            if said_number not in numbers_dict:
                numbers_dict[said_number] = [i]
            else:
                numbers_dict[said_number].append(i)
        # non starting numbers
        elif i > len(starting_nums):
            prev_number = all_spoken[-1]
            if len(numbers_dict[prev_number]) == 1:
                said_number = 0
                if said_number not in numbers_dict:
                    numbers_dict[said_number] = [i]
                else:
                    numbers_dict[said_number].append(i)
                all_spoken.append(said_number)
            elif len(numbers_dict[prev_number]) > 1:
                said_number = numbers_dict[prev_number][-1] - numbers_dict[prev_number][-2]
                all_spoken.append(said_number)
                if said_number not in numbers_dict:
                    numbers_dict[said_number] = [i]
                else:
                    numbers_dict[said_number].append(i)

    return all_spoken


def main():
    all_numbers_said = memory_game(starting_numbers)
    print(all_numbers_said)
    print("2020th number spoken is {0}".format(all_numbers_said[-1]))


if __name__ == '__main__':
    main()
