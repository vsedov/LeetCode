#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 1025_divgame
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from functools import cache

import pyinspect as pi


class Solution:
    @cache
    def divisorGame(self, n: int) -> bool:

        main_number = n

        if n == 2:
            return True

        for i in range(1, n):
            if main_number % i == 0:
                n -= i

        return (main_number % 2) == 0

        # return (n % 2) == 0


def main() -> None:
    print(Solution().divisorGame(6))


if __name__ == "__main__":
    pi.install_traceback()
    main()
