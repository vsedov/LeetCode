#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: NumOfPairs
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from collections import defaultdict
from typing import List

import pyinspect as pi
from icecream import ic


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # element_ammount = Counter(nums)

        # pairs = 0
        # for k, v in element_ammount.items():
        #     pairs += v * (v - 1) // 2

        # return pairs
        # #Solution above works , but is not a good solution

        # In this case you could use a default dict , which would be faster

        pairs = defaultdict(int)

        num = 0

        # you would count from the previous value
        # Which would then add up to all the pairs , that are the same
        for v in nums:
            ic(pairs[v])
            num += pairs[v]
            ic(num, v)

            pairs[v] += 1
        return num


def main() -> None:
    print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
    print(Solution().numIdenticalPairs([1, 1, 1, 1]))

    # 1+1 = 2 + 1 = 3 + 1 =4 + 1 = 5 + 1 = 6


if __name__ == "__main__":
    pi.install_traceback()
    main()
