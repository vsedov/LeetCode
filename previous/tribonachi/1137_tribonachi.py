#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 1137_tribonachi
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import pyinspect as pi


class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        elif n in [1, 2]:
            return 1

        dp = [float("inf") for _ in range(n + 1)]

        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[-1]


def main() -> None:
    print(Solution().tribonacci(25))


if __name__ == "__main__":
    pi.install_traceback()
    main()
