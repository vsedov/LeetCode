#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: maxlengofrepeated_subarray
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        if nums1 == nums2:
            return len(nums1)

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len_1 = len(nums1)
        len_2 = len(nums2)

        dp = [[0] * (len_1 + 1) for i in range(len_2)]

        container = 0
        for i in range(len_1):
            for j in range(len_2):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    container = max(container, dp[i][j])
        return container


def main() -> None:

    print(Solution().findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4]))


if __name__ == "__main__":
    main()
