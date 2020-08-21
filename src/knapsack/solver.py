#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple

Item = namedtuple("Item", ["index", "value", "weight"])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split("\n")

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    # value, taken = trivial_solution(items,capacity)
    value, taken = dynamic_programming_solution_tabular(items, capacity)
    # prepare the solution in the specified output format
    output_data = str(value) + " " + str(0) + "\n"
    output_data += " ".join(map(str, taken))
    return output_data


def trivial_solution(items, capacity):
    # a trivial algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0] * len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return value, taken


def dynamic_programming_solution(items, capacity):
    pass


def dynamic_programming_solution_tabular(items, capacity):
    table = [[0] * (len(items) + 1) for _ in range(capacity + 1)]
    taken = [0] * len(items)

    for col in range(len(table[0])):
        for row in range(len(table)):
            if col == 0:
                table[row][col] = 0
            else:
                current_item = items[col - 1]
                # case 1: item does not fit
                if row < current_item.weight:
                    table[row][col] = table[row][col - 1]
                # case 2: item fits, and we either do not take it and go with prev max, or take it and subtract the weight of it
                else:
                    table[row][col] = max(
                        table[row][col - 1],
                        current_item.value + table[row - current_item.weight][col - 1],
                    )

    curr_row = len(table) - 1
    max_val = table[curr_row][-1]

    for col in range(len(table[0]) - 1, 0, -1):
        if table[curr_row][col] == table[curr_row][col - 1]:
            taken[col - 1] = 0
        else:
            taken[col - 1] = 1
            curr_row -= items[col - 1].weight

    return max_val, taken


def branch_and_bound(relaxation_config):
    pass


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, "r") as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            "This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)"
        )
