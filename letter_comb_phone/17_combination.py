#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 17_combination.py

from typing import List

import pyinspect as pi


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = [""]
        for i in digits:
            res = [result + d for result in res for d in digit_map[i]]
        return res


def main() -> None:
    print(Solution().letterCombinations("23"))


if __name__ == "__main__":
    pi.install_traceback()
    main()
