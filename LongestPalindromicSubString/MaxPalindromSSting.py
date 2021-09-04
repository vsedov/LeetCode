#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: MaxPalindromSSting
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from functools import cache

from icecream import ic


class Solution:
    def is_palidrom(self, string: str) -> bool:
        return string == string[::-1]

    @cache
    def longestPalindrome(self, s: str) -> str:

        # we check the whole string first

        # ALl of this is really shit or just takes too long , you need a way to
        # do this faster Viv
        if self.is_palidrom(s):
            return s

        string_length = len(s)

        if string_length == 0:
            return ""

        container = (
            s[i:j]
            for i in range(string_length)
            for j in range(i + 1, string_length + 1)
            if self.is_palidrom(s[i:j])
        )

        return max(container, key=len)

    @cache
    def long_faster(self, s: str) -> str:

        # Little harder to get head around but dp solution is indeed faster
        longest_palindrome = ""
        length = len(s)
        dp = [[0] * length for _ in range(length)]

        for i in range(length):
            # All diagnoal is true
            dp[i][i] = True
            longest_palindrome = s[i]

        ic(dp)
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                # previous vaues are the same
                # We then index the values
                if (s[i] == s[j]) and (j - i == 1 or dp[i + 1][j - 1] is True):

                    dp[i][j] = True

                    if len(longest_palindrome) < len(s[i : j + 1]):
                        longest_palindrome = s[i : j + 1]
        ic(dp)

        return longest_palindrome


def main() -> None:
    print(Solution().long_faster("dbbdx"))


if __name__ == "__main__":
    main()

    # container = set()
    # for i in range(string_length):
    #     for j in range(i + 1, string_length + 1):
    #         if self.is_palidrom(x := (s[i:j])):
    #             container.add(x)

    # container = (
    #
    #     s[i:j]
    #     for i, j in combinations(range(string_length + 1), 2)
    #     if self.is_palidrom(s[i:j])
    # )

    # return max(container, key=len)
