#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: CountVowels
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from collections import defaultdict
from functools import cache

import pyinspect as pi


class Solution:
    @cache
    def countVowelStrings(self, n: int) -> int:
        dp = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}

        if n == 1:
            return len(dp.keys())

        vowel_map = {
            "$": list(dp.keys()),
            "a": ["a", "e", "i", "o", "u"],
            "e": ["e", "i", "o", "u"],
            "i": ["i", "o", "u"],
            "o": ["o", "u"],
            "u": ["u"],
        }

        # We are creating a dp map , with  the previous values

        # No Mode value is required

        for _ in range(n - 1):
            next_dp = defaultdict(int)
            for key, value in dp.items():
                next_letter = vowel_map[key]
                for letter in next_letter:
                    next_dp[letter] = next_dp[letter] + value

            dp = next_dp

        return sum(dp.values())


def main() -> None:
    print(Solution().countVowelStrings(3))


if __name__ == "__main__":
    pi.install_traceback()
    main()
