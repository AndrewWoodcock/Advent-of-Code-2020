
# from collections import deque

cup_input = [3, 8, 9, 1, 2, 5, 4, 6, 7]


class Cup:

    def __init__(self, label: int):
        self.label = label


class CupDeck:

    def __init__(self):
        self.cup_deck = []

    def populate_deck(self, cup_list: list):
        for cup in cup_list:
            self.add_cup(Cup(cup))

    def add_cup(self, cup: Cup):
        self.cup_deck.append(cup)

    def cup_labels(self):
        return [cup.label for cup in self.cup_deck]

    def min_cup(self):
        return min(self.cup_labels())

    def max_cup(self):
        return max(self.cup_labels())


def pick_three(cups: CupDeck, current_cup: Cup):
    deck_len = len(cups.cup_deck) - 1
    curr_index = cups.cup_deck.index(current_cup) + 1

    # get the next 3 indexes
    next_three = CupDeck()
    for i in range(1, 4):
        if curr_index + 1 <= deck_len:
            next_index = curr_index
            next_cup = cups.cup_deck.pop(next_index)
            next_three.add_cup(next_cup)
        else:
            next_index = 0
            next_cup = cups.cup_deck.pop(next_index)
            next_three.add_cup(next_cup)
            curr_index = 0
    return next_three


def find_destination(cups: CupDeck, current_cup: Cup, picked_three: CupDeck) -> int:
    min_cup = cups.min_cup()
    max_cup = cups.max_cup()
    target_label = current_cup.label - 1
    target_found = False

    while target_found is False:
        if target_label in cups.cup_labels():
            target_found = True
            print("Destination: {0}".format(target_label))
            return cups.cup_labels().index(target_label) + 1
        elif (target_label - 1) < min_cup:
            target_found = True
            print("Destination: {0}".format(max_cup))
            return cups.cup_labels().index(max_cup) + 1
        else:
            target_label -= 1



def insert_cups(cups: CupDeck, inserting: CupDeck, dest: int):
    i = 0
    for element in reversed(inserting.cup_deck):
        if dest == 1:
            if i == 0:
                cups.cup_deck.insert(dest - 1, element)
                i += 1
            else:
                max_cup = len(cups.cup_deck)
                cups.cup_deck.insert(max_cup - 1, element)
        else:
            cups.cup_deck.insert(dest, element)


def main():
    # create cups deck
    cups = CupDeck()
    # fill cups deck from given input
    cups.populate_deck(cup_input)
    print("Start")
    print(cups.cup_labels())
    for i in range(0, 3):
        move = i + 1
        print("Move {0}".format(move))
        # get the next three cups
        picked_three = pick_three(cups, cups.cup_deck[i])
        print("Pick up: {0}".format(picked_three.cup_labels()))
        # find the destination
        destination = find_destination(cups, cups.cup_deck[i], picked_three)
        print("Destination index is {0}".format(destination - 1))
        insert_cups(cups, picked_three, destination)
        print(cups.cup_labels())


if __name__ == '__main__':
    main()
