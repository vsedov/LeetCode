#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 128_longest.py

from typing import List

import pyinspect as pi


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # First you have to srot the infomation

        if not nums:
            return 0
        arr = sorted(nums)

        prev, current, longest = arr[0], 1, 1

        for i in range(1, len(arr)):

            if prev + 1 == arr[i]:
                current += 1

            elif prev + 1 != arr[i] and prev != arr[i]:
                longest = max(longest, current)
                current = 1

            prev = arr[i]
        return max(longest, current)


# class Solution:
#     def longestConsecutive(self, nums):
#         if not nums:
#             return 0

#         nums.sort()

#         longest_streak = 1
#         current_streak = 1

#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]:
#                 if nums[i] == nums[i - 1] + 1:
#                     current_streak += 1
#                 else:
#                     longest_streak = max(longest_streak, current_streak)
#                     current_streak = 1

#         return max(longest_streak, current_streak)


def main() -> None:
    print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9)
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
    print(Solution().longestConsecutive([0, -1]) == 2)
    print(Solution().longestConsecutive([0]) == 1)
    print(Solution().longestConsecutive([]) == 0)
    print(Solution().longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]) == 7)

    pass


if __name__ == "__main__":
    pi.install_traceback()
    main()
