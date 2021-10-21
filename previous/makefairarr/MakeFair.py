#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: MakeFair
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


class Solution:
    # def waysToMakeFair_try_1(self, nums: List[int]) -> int:

    #     count = 0
    #     for i in range(len(nums)):
    #         new_arr = nums[:i] + nums[i + 1 :]
    #         odd, even = 0, 0
    #         for val in range(len(new_arr)):
    #             if val % 2 == 0:
    #                 even += new_arr[val]
    #             elif val % 2 == 1:
    #                 odd += new_arr[val]

    #         if odd == even:
    #             count += 1

    #     return count

    # def waysToMakeFair(self, nums: List[int]) -> int:

    #     count = 0
    #     i = 0

    #     while i < len(nums):
    #         arr = nums[:i] + nums[i + 1 :]

    #         even = sum(arr[::2])
    #         odd = sum(arr[1::2])

    #         if even == odd:
    #             count += 1

    #         i += 1
    #     return count

    def waysToMakeFair(self, nums: List[int]) -> int:
        count = 0
        deleted = []
        even, odd = 0, 0

        for i, val in enumerate(nums):
            deleted.append((odd, even))

            if i % 2:
                odd += val
            else:
                even += val

        # reset even and odd

        even, odd = 0, 0

        for i in range(len(nums) - 1, -1, -1):
            if deleted[i][0] + even == deleted[i][1] + odd:
                count += 1
            if i % 2:
                odd += nums[i]
            else:
                even += nums[i]

        return count


def main() -> None:
    # This should return 1
    print(Solution().waysToMakeFair([2, 1, 6, 4]) == 1)
    print(Solution().waysToMakeFair([1, 1, 1]) == 3)
    print(Solution().waysToMakeFair([1, 2, 3]) == 0)


if __name__ == "__main__":
    pi.install_traceback()
    main()

    #     temp = nums.copy()
    #     contain = 0
    #     for index, i in enumerate(nums):

    #         temp.pop(index)

    #         odd = 0
    #         even = 0

    #         for val in range(len(temp)):
    #             if val % 2 == 1:
    #                 odd += temp[val]

    #             elif val % 2 == 0:
    #                 even += temp[val]

    #         if even == odd:
    #             contain += 1

    #         temp = nums.copy()

    #     return contain
    #
