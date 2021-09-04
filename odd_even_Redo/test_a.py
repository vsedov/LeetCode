#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: test_a
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import pyinspect as pi

from Odd_even_jump import Solution


def test_a() -> None:
    sol = Solution(arr=[10, 13, 12, 14, 15])
    x = sol.oddEvenJumps()
    assert x == 2


def test_b() -> None:

    sol = Solution(arr=[2, 3, 1, 1, 4])

    x = sol.oddEvenJumps()
    assert x == 3


def test_c() -> None:
    sol = Solution(arr=[5, 1, 3, 4, 2])
    assert sol.oddEvenJumps() == 3


def main() -> None:
    test_a()
    # test_b()


if __name__ == "__main__":
    pi.install_traceback()
    main()

"""
Input: arr = [10,13,12,14,15]
Output: 2
Explanation: 
From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
From starting index i = 4, we have reached the end already.
In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
jumps.
"""
