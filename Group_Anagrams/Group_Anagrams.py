#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: Group_Anagrams
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from collections import defaultdict
from typing import List

import pyinspect as pi
from icecream import ic


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        main_d = defaultdict(list)

        for i in strs:
            key = "".join(sorted(i))
            ic(key, i)
            main_d[key].append(i)

        return list(main_d.values())


def main() -> None:
    Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])


if __name__ == "__main__":
    pi.install_traceback()
    main()
