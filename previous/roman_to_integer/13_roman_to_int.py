#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 13_roman_to_int
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import pyinspect as pi


class Solution:
    def romanToInt(self, s: str) -> int:

        prev = summed = 0
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for i in s[::-1]:

            if roman[i] >= prev:
                summed += roman[i]
            else:
                summed -= roman[i]
            prev = roman[i]
        return summed


def main() -> None:

    x = Solution()

    # assert x.romanToInt("III") == 3
    # assert x.romanToInt("IV") == 4
    print(x.romanToInt("XXX"))


if __name__ == "__main__":
    pi.install_traceback()
    main()
