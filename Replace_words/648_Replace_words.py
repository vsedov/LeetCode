#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: 648_Replace_words
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # this is without a dict

        # for i in str_tolist:
        #     for j in dictionary:

        #         if i.startswith(j, 0, 5):
        #             str_tolist[str_tolist.index(i)] = j

        # return " ".join(str_tolist)

        str_tolist = sentence.split()
        to_dict = set(dictionary)

        for i in range(len(str_tolist)):
            for j in range(len(str_tolist[i])):
                temp = str_tolist[i][:j]
                if temp in to_dict:
                    str_tolist[i] = temp
                    break
        return " ".join(str_tolist)


def main() -> None:
    print(
        Solution().replaceWords(
            dictionary=["a", "aa", "aaa", "aaaa"],
            sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa",
        )
    )
    pass


if __name__ == "__main__":
    pi.install_traceback()
    main()
