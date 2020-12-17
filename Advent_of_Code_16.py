
dep_rules = "departure_rules.txt"
# dep_rules = "departure_rules_test.txt"

# nearby_tickets = "nearby_tickets_test.txt"
nearby_tickets = "nearby_tickets.txt"


def get_departure_rules(filename: str) -> dict:
    rules_dict = {}
    with open(filename, "r") as file:
        for line in file:
            # split by :
            split_rule = line.split(":")
            # get dict key
            rule_key = split_rule[0].strip()
            rules_dict[rule_key] = []
            # get rule values
            rule_value_str = "".join(split_rule[1].split("or")).strip()
            split_rule_values = rule_value_str.split(" ")
            # value range 1
            rule_value_set_1 = split_rule_values[0]
            rules_dict[rule_key].append(int(rule_value_set_1.split("-")[0]))
            rules_dict[rule_key].append(int(rule_value_set_1.split("-")[1]))
            # value range 2
            rule_value_set_2 = split_rule_values[2]
            rules_dict[rule_key].append(int(rule_value_set_2.split("-")[0]))
            rules_dict[rule_key].append(int(rule_value_set_2.split("-")[1]))
    return rules_dict


def get_nearby_tickets(filename: str) -> list:
    with open(filename, "r") as file:
        ticket_list = []
        for line in file:
            ticket_list.append([int(i) for i in line.strip().split(",")])
        return ticket_list


def create_valid_numbers(rules: dict) -> set:
    valid_set = set()
    for key, value in rules.items():
        for i in range(value[0], value[1]+1):
            valid_set.add(i)
        for i in range(value[2], value[3]+1):
            valid_set.add(i)
    return valid_set


def check_validity(tickets: list, valid_numbers: set) -> list:
    error_list = []
    for ticket in tickets:
        for value in ticket:
            if value not in valid_numbers:
                error_list.append(value)
    return error_list


def main():
    departure_rules_dict = get_departure_rules(dep_rules)
    nearby_tickets_list = get_nearby_tickets(nearby_tickets)
    valid_numbers_set = create_valid_numbers(departure_rules_dict)
    ts_error_rate = sum(check_validity(nearby_tickets_list, valid_numbers_set))
    print("The ticket scanning error rate is {0}".format(ts_error_rate))


if __name__ == '__main__':
    main()
