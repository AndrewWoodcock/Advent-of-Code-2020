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


def main():
    xmas_list = get_file_data(xmas_data)
    result = inspect_xmas(xmas_list, g_preamble)
    print("The result is {}".format(result))


if __name__ == '__main__':
    main()
