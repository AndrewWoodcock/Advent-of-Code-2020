
# nav_data = "nav_instruct_test.txt"
nav_data = "nav_instruct.txt"


class Ship:

    heading_dict = {0: "North",
                    90: "East",
                    180: "South",
                    270: "West",
                    360: "North"}

    cum_heading = 0

    def __init__(self, heading: int, ew_val: int, ns_val: int):
        self.heading = heading
        self.ew_val = ew_val
        self.ns_val = ns_val
        self.cum_heading += heading

    def get_facing(self):
        return Ship.heading_dict[self.cum_heading]

    def get_east_west(self):
        if self.ew_val > 0:
            return ["east", self.ew_val]
        elif self.ew_val < 0:
            return ["west", abs(self.ew_val)]

    def get_north_south(self):
        if self.ns_val > 0:
            return ["north", self.ns_val]
        elif self.ns_val < 0:
            return ["south", abs(self.ns_val)]


def get_file_data(filename: str) -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file]


def digest_input(instruction: str) -> list:
    command = instruction[0]
    value = int(instruction[1:])
    return [command, value]


def three_sixty(current: int, addition: int) -> int:
    if current + addition > 360:
        diff_to_three_sixty = 360 - current
        remainder_of_addition = addition - diff_to_three_sixty
        return remainder_of_addition
    else:
        return current + addition


def adjust_heading(digested_list: list, ship: Ship):
    # takes the digested list and ship and updates ship cum_heading
    if digested_list[0] == "R":
        ship.cum_heading = three_sixty(ship.cum_heading, digested_list[1])
    elif digested_list[0] == "L":
        ship.cum_heading = three_sixty(ship.cum_heading, (360 - digested_list[1]))


def move_by_direction(digested_list: list, ship: Ship):
    if digested_list[0] == "N":
        ship.ns_val += digested_list[1]
    elif digested_list[0] == "S":
        ship.ns_val -= digested_list[1]
    elif digested_list[0] == "E":
        ship.ew_val += digested_list[1]
    elif digested_list[0] == "W":
        ship.ew_val -= digested_list[1]


def move_by_forward(digested_list: list, ship: Ship):
    if digested_list[0] == "F":
        current_direction = ship.get_facing()[0]
        forward_list = [current_direction, digested_list[1]]
        move_by_direction(forward_list, ship)


def main():
    instructions = get_file_data(nav_data)
    # initiate the ship
    my_ship = Ship(90, 0, 0)

    # loop through instructions
    for instruct in instructions:
        print(instruct)
        # handle inputs
        digested = digest_input(instruct)
        # adjust heading if applicable
        adjust_heading(digested, my_ship)
        # movement
        move_by_direction(digested, my_ship)
        move_by_forward(digested, my_ship)

        print(my_ship.get_east_west())
        print(my_ship.get_north_south())

    manhattan = my_ship.get_east_west()[1] + my_ship.get_north_south()[1]
    print("The Manhattan distance is {0}".format(manhattan))


if __name__ == '__main__':
    main()
