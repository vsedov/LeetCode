#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: int_to_roman
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import pyinspect as pi


class Solution:
    def intToRoman(self, num: int) -> str:

        roman = {}

        roman[1000] = "M"
        roman[900] = "CM"
        roman[500] = "D"
        roman[400] = "CD"
        roman[100] = "C"
        roman[90] = "XC"
        roman[50] = "L"
        roman[40] = "XL"
        roman[10] = "X"
        roman[9] = "IX"
        roman[5] = "V"
        roman[4] = "IV"
        roman[1] = "I"

        roman_number = ""

        for k in roman.keys():

            while num >= k:
                roman_number += roman[k]
                num -= k

        return roman_number


def main() -> None:
    some_number = int(input("Enter a number:  "))
    print(f"{some_number} is mapped to {Solution().intToRoman(some_number)}")


if __name__ == "__main__":
    pi.install_traceback()
    main()
