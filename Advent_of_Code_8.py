# solution for part 1 only

boot_sequence = "boot.txt"
# boot_sequence = "boot_test.txt"


class Operation:
    def __init__(self, action: str, argument: int):
        self.action = action
        self.argument = argument


def get_file_data(filename: str) -> dict:
    operation_dict = {}
    with open(filename, "r") as file:
        i = 0
        for line in file:
            operation_dict[i] = []
            operation_dict[i].append(Operation(line[:3].strip(), int(line[4:].strip())))
            i += 1
    return operation_dict


def eval_action(action: str, argument: int) -> dict:
    commands = {"accumulator": 0,
                "jump": 0}
    if action == "acc":
        commands["accumulator"] += argument
        commands["jump"] += 1
    elif action == "jmp":
        commands["jump"] += argument
    else:
        commands["jump"] += 1
    return commands


def main():
    operation_dict = get_file_data(boot_sequence)

    x = 0
    accumulator = 0
    visited = []
    abort = False
    while (x <= len(operation_dict) - 1) and abort is False:
        # how to get each key
        op_index = list(operation_dict.keys())[x]
        if op_index in visited:
            abort = True
        else:
            visited.append(op_index)
            op_action = operation_dict[x][0].action
            op_argument = operation_dict[x][0].argument
            print("Key : {0}, Action : {1}, Argument : {2}".format(op_index, op_action, op_argument))

            evaluation = eval_action(op_action, op_argument)
            accumulator += evaluation["accumulator"]
            x += evaluation["jump"]

    print("Accumulator is {0}".format(accumulator))


if __name__ == '__main__':
    main()
