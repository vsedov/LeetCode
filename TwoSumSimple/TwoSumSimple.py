#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: TwoSumSimple
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, num in enumerate(nums):
            left_over = target - num
            if left_over in values:
                return [i, values[left_over]]

            else:
                values[num] = i


def main() -> None:
    print(Solution().twoSum([3, 2, 4], 6))


if __name__ == "__main__":
    pi.install_traceback()
    main()
