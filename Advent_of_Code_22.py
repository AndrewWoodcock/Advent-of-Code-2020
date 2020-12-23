
# hands_data = [[9, 2, 6, 3, 1], [5, 8, 4, 7, 10]]
hands_data = [[26, 8, 2, 17, 19, 29, 41, 7, 25, 33, 50, 16, 36, 37, 32, 4, 46, 12, 21, 48, 11, 6, 13, 23, 9],
              [27, 47, 15, 45, 10, 14, 3, 44, 31, 39, 42, 5, 49, 24, 22, 20, 30, 1, 35, 38, 18, 43, 28, 40, 34]]


class Card:

    def __init__(self, rank: int):
        self.rank = rank


class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)


def pop_hand(card_list: list, hand: Hand):
    for card in card_list:
        hand.add_card(Card(card))


def compare_cards(p1_hand: Hand, p2_hand: Hand):
    p1_next_card = p1_hand.cards[0].rank
    p2_next_card = p2_hand.cards[0].rank

    if p1_next_card > p2_next_card:
        popped_1 = p1_hand.cards.pop(0)
        popped_2 = p2_hand.cards.pop(0)
        p1_hand.add_card(popped_1)
        p1_hand.add_card(popped_2)
        print("Player 1 Wins")
    elif p2_next_card > p1_next_card:
        popped_1 = p2_hand.cards.pop(0)
        popped_2 = p1_hand.cards.pop(0)
        p2_hand.add_card(popped_1)
        p2_hand.add_card(popped_2)
        print("Player 2 Wins")



def main():
    # create player 1 hand
    player_1 = Hand()
    pop_hand(hands_data[0], player_1)
    player_2 = Hand()
    pop_hand(hands_data[1], player_2)

    while player_1.cards and player_2.cards:
        compare_cards(player_1, player_2)

    if len(player_1.cards) > 0:
        winner = "Player 1"
        winning_hand = player_1
    else:
        winner = "Player 2"
        winning_hand = player_2

    print("Game finished, {0} is the Winner".format(winner))

    i = 1
    score = 0
    for card in reversed(winning_hand.cards):
        card_score = i * card.rank
        score = score + card_score
        i += 1

    print("The winning score is {0}".format(score))


if __name__ == '__main__':
    main()
