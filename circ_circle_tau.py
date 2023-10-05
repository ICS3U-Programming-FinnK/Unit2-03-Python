#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: September 27th, 2023
# This program asks the user for the radius of
# a circle in cm. It then calculates and displays
# the circumference using tau.
import constants


def main():
    # user imputs the radius into the terminal
    radius = float(input("Enter the radius of the circle (cm): "))

    # terminal calculates the circumference
    circumference = constants.TAU * radius

    # terminal displays the circumference
    print("")
    print("Circumference = {} cm".format(circumference))


if __name__ == "__main__":
    main()
