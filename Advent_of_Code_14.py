
# bitmask_file = "bitmask_test.txt"
bitmask_file = "bitmask.txt"


def get_file_data(filename: str) -> list:
    with open(filename, "r") as file:
        return [line.strip().split(" ") for line in file]


def write_to_memory(bit_list: list) -> dict:
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    memory_dict = {}
    for element in bit_list:
        if element[0] == "mask":
            mask = element[2]
        else:
            memory_location = element[0]
            bits = "{:036b}".format(int(element[2]))
            masked_bits = []
            for i, j in zip(mask, bits):
                if i == "X":
                    masked_bits.append(j)
                else:
                    masked_bits.append(i)
            memory_dict[memory_location] = int("".join(masked_bits), 2)
    return memory_dict


def main():
    # extract data
    bitmask_list = get_file_data(bitmask_file)
    # run masking
    memory = write_to_memory(bitmask_list)
    print(memory)
    memory_sum = sum(memory.values())
    print(memory_sum)


if __name__ == '__main__':
    main()

