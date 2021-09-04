#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: Test
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import pyinspect as pi
from icecream import ic


def main() -> None:
    x = [1, 2, 3, 4, 5, 6]

    for i in range(2, len(x) + 1):
        ic(x[i - 1 : i], x[i - 2 : i])


"""

    When you want a unique value , for each pointer within the list , we would use i -1 within range of i
    If we want the next two given values , or the two given substring , we would take those values instead . 

    than what you would get is teh following , you would get all possible optionsiwthin teh next values from 1 2 2 3 and so on 
    if you did i - 2 : i 

    , which is kinda cool , while x - 1 : i will only give 2 to the given length, the other one will not , which i found rather interesting 

    what you would end up having is a list of indomation that would be get updated overtime , or where you would add teh values onto each other , for how ever many pointers you have

"""


if __name__ == "__main__":
    pi.install_traceback()
    main()
