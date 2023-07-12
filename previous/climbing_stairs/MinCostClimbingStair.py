#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: MinCostClimbingStair
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0

        dp = [0] * len(cost)

        dp[0], dp[1] = cost[0], cost[1]

        for i in range(2, len(cost)):

            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[-1], dp[-2])


def main() -> None:
    print(Solution().minCostClimbingStairs([10, 15, 20]))
    print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))


if __name__ == "__main__":
    pi.install_traceback()
    main()
