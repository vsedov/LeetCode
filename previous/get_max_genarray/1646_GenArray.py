#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 1646_GenArray
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


from functools import cache


class Solution:
    @cache
    def getMaximumGenerated(self, n: int) -> int:

        # One of the main base cases
        if n in {0, 1}:
            return n

        dp, max_val = [0] * (n + 1), 0
        dp[0], dp[1] = 0, 1

        for i in range(2, n + 1):

            if i % 2 == 0:
                dp[i] = dp[i // 2]

            elif i % 2 == 1:
                dp[i] = dp[i // 2] + dp[(i // 2) + 1]

            max_val = max(dp[i], max_val)

        return max_val


def main() -> None:
    print(Solution().getMaximumGenerated(n=10))


if __name__ == "__main__":
    main()
