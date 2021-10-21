#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: MaxScore
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


from functools import cache

import pyinspect as pi


class Solution:
    __slots__ = "s", "x", "y"

    # Allows the process to be faster- kinda cheating ngl , but if you can do it
    # why not right ?
    @cache
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # to calculate first, high value of x or y
        a, b = "ab", "ba"
        if y > x:
            b, a = a, b
            y, x = x, y

        answer = 0

        # This idea is kinda cool, never seen it before
        for word in [a, b]:
            main_stack = []

            for i in range(0, len(s)):
                main_stack.append(s[i])
                legnth = len(main_stack)

                # Comapring the last two values within the given list
                prefex = (main_stack[legnth - 2]) + (main_stack[legnth - 1])

                if prefex == word:
                    answer += x
                    main_stack.pop()
                    main_stack.pop()
            x = y
            s = "".join(main_stack)
        return answer


def main() -> None:

    x = sol = Solution().maximumGain("ababababbbababababababbabababababababab", 10, 30)
    print(x)


if __name__ == "__main__":
    pi.install_traceback()
    main()


"""
    Remove ab and gain x points
    remove ba and you get y points
"""
