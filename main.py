#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program uses a while loop to solve the power of ever number
#   up to the inputed number


def main():
    # this function uses a while loop to solve the power of ever number
    #   up to the inputed number

    # this is to keep track of how many times you go through the loop
    loop_counter = 0

    # input
    print("\n", end="")
    positive = input("Enter an integer to power: ")

    # process & output
    try:
        positive_int = int(positive)
        print("\n", end="")
        while loop_counter <= positive_int:

            powered_number = loop_counter ** 2

            print("{0}² = {1}".format(loop_counter, powered_number))

            loop_counter = loop_counter + 1

    except Exception:
        print("\nYou have entered an invalid integer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
