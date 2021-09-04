#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 118_PTriangle
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:  # noqa:ignore

        if numRows == 1:
            return [[1]]

        dp = [[] for _ in range(numRows)]

        dp[0] = [1]
        dp[1] = [1, 1]

        for i in range(2, numRows):

            prev = dp[i - 1]
            dp[i].append(1)
            for previous, current in zip(prev, prev[1:]):
                dp[i].append(previous + current)
            dp[i].insert(len(dp[i]), 1)

        return dp

    def generate_NotMine_Improv(self, numRows: int) -> List[List[int]]:  # noqa:ignore

        dp = [[1] * (i + 1) for i in range(numRows)]

        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

        return dp


def main() -> None:

    print(Solution().generate_NotMine_Improv(0))
    # print(Solution().generate(2))


if __name__ == "__main__":
    pi.install_traceback()
    main()
