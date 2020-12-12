
adapters = "adapters.txt"
# adapters = "adapters_test.txt"


def get_file_data(filename: str) -> list:
    with open(filename, "r") as file:
        return [int(line) for line in file]


def organise_adapters(bag_adapter_list: list) -> list:
    bag_adapter_list.append(0)
    bag_adapter_list.append(max(bag_adapter_list) + 3)
    sorted_list = sorted(bag_adapter_list)
    return sorted_list


def count_jolt(sorted_adapter_list: list) -> list:
    jolt_dict = {1: [],
                 2: [],
                 3: []}
    out_list = []
    max_el = len(sorted_adapter_list) - 1
    for element in enumerate(sorted_adapter_list):
        if element[0] + 1 > max_el:
            break
        else:
            this_index = element[1]
            next_index = sorted_adapter_list[element[0] + 1]
            delta = next_index - this_index
            jolt_dict[delta].append(1)
    out_list.append(len(jolt_dict[1]))
    out_list.append(len(jolt_dict[3]))
    return out_list


def main():
    adapter_list = get_file_data(adapters)
    sorted_adapter_list = organise_adapters(adapter_list)
    print(sorted_adapter_list)
    result_1_list = count_jolt(sorted_adapter_list)
    result_1 = result_1_list[0] * result_1_list[1]
    print("Result is {0}".format(result_1))


if __name__ == '__main__':
    main()
