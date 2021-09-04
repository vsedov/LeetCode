#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: another_solution.py

from typing import List, Union

import pyinspect as pi


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        backtrack = Union[int, str]

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

        def backtrack(index: int, current: str) -> backtrack:  # noqua:ignore
            if len(current) == len(digits):
                res.append(current)
                return

            for i in digit_map[digits[index]]:
                backtrack(index + 1, current + i)

        if digits:
            backtrack(0, "")

        return res


def main() -> None:

    print(Solution().letterCombinations("23"))


if __name__ == "__main__":
    pi.install_traceback()
    main()
