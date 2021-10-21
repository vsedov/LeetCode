#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: VowelCount
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


from collections import defaultdict


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowel_map = {
            "$": ["a", "e", "i", "o", "u"],  # '$' is used only as a starting symbol.
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"],
        }

        dp = {
            "a": 1,
            "e": 1,
            "i": 1,
            "o": 1,
            "u": 1,
        }

        mod_value = pow(10, 9) + 7
        for _ in range(n - 1):

            next_dp = defaultdict(int)
            for key, val in dp.items():
                next_letter = vowel_map[key]
                for letter in next_letter:

                    # Like doing +=1  on the list
                    next_dp[letter] = (next_dp[letter] + val) % mod_value

            dp = next_dp

        return sum(dp.values()) % mod_value


def main() -> None:

    print(Solution().countVowelPermutation(5))


if __name__ == "__main__":
    main()
