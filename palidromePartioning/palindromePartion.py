#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: palindromePartion
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi
from icecream import ic


class Solution:
    def is_palindrome(self, string: str) -> bool:
        return string == string[::-1]

    def partition(self, s: str) -> List[List[str]]:

        length = len(s)

        dp = [[] for _ in range(length + 1)]

        dp[-1] = [[]]  # You are pushing everything into this part of the list
        ic(dp)

        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length + 1):
                word = s[i:j]
                if self.is_palindrome(word):
                    for l in dp[j]:
                        dp[i].append([word] + l)

        return dp[0]


def main() -> None:
    print(Solution().partition("aabaac"))


if __name__ == "__main__":
    pi.install_traceback()
    main()
