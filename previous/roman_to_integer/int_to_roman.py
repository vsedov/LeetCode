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

        roman = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        roman_number = ""

        for k in roman:

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
