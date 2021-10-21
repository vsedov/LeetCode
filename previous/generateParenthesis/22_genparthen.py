#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 22_genparthen
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from functools import lru_cache
from typing import List

import pyinspect as pi


class Solution:
    @lru_cache
    def generateParenthesis(self, n: int) -> List[str]:

        main_stack, current_string = [], ""

        def backtracker(
            main_stack: List[str], current: str, open: int, close: int
        ) -> None:
            # we have some base case
            if len(current) == 2 * n:
                main_stack.append(current)
                return

            if open < n:
                backtracker(main_stack, current + "(", open + 1, close)

            if close < open:
                backtracker(main_stack, current + ")", open, close + 1)

        backtracker(main_stack, current_string, 0, 0)

        return main_stack

    # Both do the same  thing , with respect to the stack , we arent doing any
    # extra operations , we are just pushing through data into it
    def gen(self, n: int) -> List[str]:

        main_stack, res = [], []

        def backtracker(open: int, close: int) -> None:
            if open == close == n:
                res.append("".join(main_stack))
                return

            if open < n:
                main_stack.append("(")
                backtracker(open + 1, close)
                main_stack.pop()

            if close < open:
                main_stack.append(")")
                backtracker(open, close + 1)
                main_stack.pop()

        backtracker(0, 0)

        return res


def main() -> None:
    print(Solution().generateParenthesis(3))
    print(Solution().gen(3))


if __name__ == "__main__":
    pi.install_traceback()
    main()
