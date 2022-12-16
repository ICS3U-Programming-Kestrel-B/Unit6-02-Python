#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Dec. 15, 2022
# This program generates 10
# random numbers from 1 to
# 100 and calculates the
# highest number

import math
import random


def max_value(random_num_list):
    # initializing max_num
    max_num = -1
    # if random_num_list[0] > random_num_list[1]:
    for counter in range(10):
        current_num = random_num_list[counter]
        if current_num > max_num:
            max_num = current_num
    # returning max_num
    return max_num


def main():
    # introductory paragraph
    print("This program generates 10")
    print("random numbers from 1 to")
    print("100 and calculates the")
    print("highest number")
    print("")

    # initializing variables
    random_num_list = []

    # generating numbers
    for counter in range(0, 10):
        random_num = random.randint(0, 100)
        random_num_list.append(random_num)
        # displaying generated number
        print("{} has been generated.".format(random_num))

    # calling function
    true_max = max_value(random_num_list)

    # displaying results
    print("The highest number is {}.".format(true_max))


if __name__ == "__main__":
    main()
