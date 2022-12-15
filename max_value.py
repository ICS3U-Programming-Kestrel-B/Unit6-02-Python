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
    if random_num_list[0] > random_num_list[1]:
        


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

    # displaying results
    print("The highest number is {}.".format(avg))


if __name__ == "__main__":
    main()
