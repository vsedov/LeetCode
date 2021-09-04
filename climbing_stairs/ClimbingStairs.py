#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: ClimbingStairs
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from functools import cache

import pyinspect as pi


# Proud of this , starting this out , properly , nicely coded ,with the i -2
# - where were are storing value in the given range
class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        prev, second_prev = 1, 1
        for i in range(n - 1, -1, -1):
            prev, second_prev = (prev + second_prev), prev

        return second_prev

    @cache
    def climbstairs_with_dp(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]

        # Creating a base case
        dp[-1] = 1
        dp[-2] = 1

        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]


def main() -> None:
    print(Solution().climbStairs(5))
    print(Solution().climbstairs_with_dp(5))


if __name__ == "__main__":
    pi.install_traceback()
    main()
