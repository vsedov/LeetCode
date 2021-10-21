#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 20_validparen
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


from functools import cache

from icecream import ic


class Solution:
    @cache
    def isValid(self, s: str) -> bool:

        left = "({["
        right = ")}]"
        main_stack = []

        for i in s:

            if i in left:
                main_stack.append(i)

            elif not main_stack or left.find(main_stack.pop()) != right.find(i):
                return False

        return not main_stack


def main() -> None:
    print(Solution().isValid("[[]"))


if __name__ == "__main__":
    main()


def example() -> None:
    stack = ["["]

    # Ahh you pop the nearest on
    ic(left.find(stack.pop()))

    ic(right.find("]"))
