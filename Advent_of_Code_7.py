# not solved

import pprint as pp

# rule_file = "rules.txt"
rule_file = "rules_test.txt"


def get_file_data(filename: str) -> dict:
    with open(filename, "r") as file:
        parent_child_dict = {}
        for line in file:
            parent_bag = line.split("bags contain")[0].strip()
            child_bags = "".join(line.split("bags contain")[1:]).strip().split(", ")
            parent_child_dict[parent_bag] = []
            for bag in child_bags:
                bag = bag.strip(".")
                if bag == "no other bags":
                    pass
                else:
                    bag = bag.strip("bags").strip()
                    # get list
                    parent_child_dict[parent_bag].append(bag[2:])
                    # get list of dicts
                    # parent_child_dict[parent_bag].append({bag[2:]: int(bag[0])})

        return parent_child_dict


def depth_first_search(graph, source, path=[]):
    # if source not in path:
    #     path.append(source)
    path.append(source)
    for neighbour in graph[source]:
        path = depth_first_search(graph, neighbour, path)

    return path


def find_bag(dictionary: dict, bag, found=[]):
    for k, v in dictionary.items():
        if k in found:
            found.append(k)
        else:
            found.append(k)
            for sub in dictionary[k]:
                find_bag(dictionary, bag, found)
    return found


def search_shiny(bags_dict: dict) -> int:
    cnt = 0
    for key, value in bags_dict.items():
        for bag in value:
            if bag == "shiny gold":
                cnt += 1
            elif bag != "shiny gold":
                for sub_bag in bags_dict[bag]:
                    if sub_bag == "shiny gold":
                        cnt += 1
                        break
            break

    return cnt


def main():
    temp_dict = get_file_data(rule_file)
    print(temp_dict)
    # print(depth_first_search(temp_dict, next(iter(temp_dict))))
    print(find_bag(temp_dict, "shiny gold"))





    #177


if __name__ == '__main__':
    main()
