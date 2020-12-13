
# bus_times = "bus_timetable_test.txt"
bus_times = "bus_timetable.txt"


def get_file_data(filename: str) -> list:
    with open(filename, "r") as file:
        return [line.strip() for line in file]


def project_times(timetable: list, start: int, interval: int) -> list:
    # got a bit over max to be safe
    range_max = start + (interval * 2) + 5
    for i in range(0, range_max):
        for bus in timetable:
            # if i % bus == 0:
            #     print("Time: {0}, Bus: {1}".format(i, bus))
            if (i > start) and (i % bus == 0):
                print("Time: {0}, Bus: {1}".format(i, bus))
                return [i, bus]


def main():
    bus_data = get_file_data(bus_times)
    earliest_time = int(bus_data[0])
    timetable = bus_data[1].split(",")
    # make a list of just the active buses
    active_timetable = [int(element) for element in timetable if element.isnumeric()]
    # get the max so we know how high the range needs to go past
    max_interval = max(active_timetable)
    earliest_bus = project_times(active_timetable, earliest_time, max_interval)
    # get result
    time_to_wait = earliest_bus[0] - earliest_time
    id_times_wait = earliest_bus[1] * time_to_wait
    print(id_times_wait)




if __name__ == '__main__':
    main()
