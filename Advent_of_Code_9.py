# Part 1 Unsolved
import itertools

# xmas_data = "xmas_test.txt"
xmas_data = "xmas.txt"

# g_preamble = 5
g_preamble = 25


def get_file_data(filename: str) -> list:
    with open(filename, "r") as file:
        return [int(line.strip()) for line in file]


def check_sum(lst: list, num: int) -> bool:
    for x, y in itertools.combinations(lst, 2):
        if x + y == num:
            return True
    return False


def inspect_xmas(full_list: list, preamble: int) -> int:
    for element in enumerate(full_list):
        if element[0] >= preamble:
            test = element[1]
            test_list = full_list[(element[0] - preamble):element[0]]
            if not check_sum(test_list, test):
                return element[1]


def find_less_reverse(full_list: list, target: int) -> int:
    for element in reversed(list(enumerate(full_list))):
        if element[1] < target:
            return element[0]


def encrypt_weakness(trimmed_list: list, sum_target: int) -> int:
    i = 0
    j = 1
    curr_sum = trimmed_list[i] + trimmed_list[j]
    while curr_sum != sum_target:
        while curr_sum < sum_target:
            j += 1
            curr_sum += trimmed_list[j]
        while curr_sum > sum_target:
            curr_sum -= trimmed_list[i]
            i += 1
    contig = sorted(trimmed_list[i:j])
    return sum([contig[0], contig[-1]])


def main():
    xmas_list = get_file_data(xmas_data)
    result_1 = inspect_xmas(xmas_list, g_preamble)
    print("The part 1 result is {}".format(result_1))
    upper_bound = find_less_reverse(xmas_list, result_1) + 1
    trimmed_xmas_list = xmas_list[:upper_bound]
    result_2 = encrypt_weakness(trimmed_xmas_list, result_1)
    print("The part 2 result is {}".format(result_2))


if __name__ == '__main__':
    main()
