#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: equal_K
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from collections import defaultdict
from typing import List

import pyinspect as pi


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        main_d = defaultdict(int)
        main_d[0] = 1
        sum = result = 0

        for i in nums:
            sum += i
            # ic(i, sum, sum - k, main_d)
            if sum - k in main_d:
                result += main_d[sum - k]

            main_d[sum] += 1
        return result

        # for i in range(len(nums)):
        #     sumr = 0

        #     for j in range(i, len(nums)):
        #         sumr += nums[j]

        #         if sumr == k:
        #             result += 1

        # print(result)


def main() -> None:
    print(Solution().subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))


if __name__ == "__main__":
    pi.install_traceback()
    main()
