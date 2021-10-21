#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 647_palindromeSubstring
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

import pyinspect as pi


class Solution:
    def countSubstrings(self, s: str) -> int:

        length = len(s)

        dp = [[0] * length for _ in range(length)]

        count = 0
        for i in range(length):
            dp[i][i] = True
            count += 1

        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                print(s[i:j])

        return count


def main() -> None:
    print(Solution().countSubstrings("abc"))


if __name__ == "__main__":
    pi.install_traceback()
    main()
