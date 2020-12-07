
question_file = "questions.txt"
# question_file = "questions_test.txt"


def get_file_data(filename):
    with open(filename, "r") as file:
        master_list = []
        for line in file:
            line = line.strip()
            soup_list = line.split()
            if len(soup_list) == 0:
                master_list.append(" ")
            else:
                for element in soup_list:
                    master_list.append(element)
    return master_list


def split_groups(seq, sep):
    g = []
    for el in seq:
        if el == sep:
            yield g
            g = []
            continue
        g.append(el)
    yield g


def count_occur(group_list: list):
    letter_dict = {}
    for element in group_list:
        for char in element:
            if char not in letter_dict:
                letter_dict[char] = 1
            else:
                letter_dict[char] += 1
    return letter_dict


def everyone_yes(group: list, input_dict: dict):
    group_size = len(group)
    yes_cnt = 0
    for key, value in input_dict.items():
        if value == group_size:
            yes_cnt += 1
    return yes_cnt


def main():
    big_list = get_file_data(question_file)
    # split big_list by " " delimiter (excluding delimiter)
    big_split_lists = list(split_groups(big_list, " "))

    yes_list = []
    for split_list in big_split_lists:
        yes_list.append(everyone_yes(split_list, count_occur(split_list)))
    all_yes = sum(yes_list)

    print("The sum is {0}".format(all_yes))


if __name__ == "__main__":
    main()
