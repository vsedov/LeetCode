#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: FibonacciDP
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from functools import cache

import pyinspect as pi


class Solution:
    @cache
    def fib(self, n: int) -> int:
        a = 0
        b = 1

        if n < 0 or n == 0:
            return 0
        elif n == 1:
            return b

        else:
            for _ in range(1, n):
                c = a + b
                a, b = b, c
            return b


def main() -> None:
    print(Solution().fib(9))


if __name__ == "__main__":
    pi.install_traceback()
    main()
