
passport_file = "boarding.txt"
# passport_file = "boarding_test.txt"


def partition(code: str, inp_max: int, lower: str, upper: str, plus: int):
    my_list = list(range(0, inp_max + 1))

    for char in code:
        if char == lower:
            slice_index = (int((my_list.index(min(my_list)) + my_list.index(max(my_list))) / 2) + plus)
            my_list = my_list[:slice_index]
        elif char == upper:
            slice_index = (int((my_list.index(min(my_list)) + my_list.index(max(my_list))) / 2) + plus)
            my_list = my_list[-slice_index:]
        else:
            pass
    return my_list[0]


def unique_id(row: int, col: int, const: int = 8):
    return (row * const) + col


def main():
    with open(passport_file, "r") as file:
        seat_id_list = []
        for line in file:
            line = line.strip()
            row_code = line[:7]
            col_code = line[-3:]

            my_row = partition(row_code, 127, "F", "B", 1)
            my_col = partition(col_code, 7, "L", "R", 1)
            my_id = unique_id(my_row, my_col)
            seat_id_list.append(my_id)

    print("The max seat id is {0}".format(max(seat_id_list)))

    # find the empty seat
    complete_list = list(range(min(seat_id_list), max(seat_id_list) + 1))
    for element in sorted(complete_list):
        if element not in seat_id_list:
            print("This empty seat is {0}".format(element))
            break


if __name__ == "__main__":
    main()

