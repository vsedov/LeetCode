#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: MaxSubArray
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        size = len(nums)

        dp = [0] * size

        dp[0] = nums[0]

        for i in range(1, size):
            if nums[i] < 1:
                continue

            dp[i] = max(dp[i - 1] * nums[i], nums[i])

        return max(dp)


def main() -> None:

    print(Solution().maxSubArray([-2, 0, -1]))


if __name__ == "__main__":
    pi.install_traceback()
    main()
