#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Viv Sedov
#
# File Name: test_a
__author__ = "Viv Sedov"
__email__ = "viv.sv@hotmail.com"


import pytest
from termcolor import colored

from Annoyingstupidquestion_substring import Solution


@pytest.fixture()
def resource() -> Solution:
    print(colored("Setup Outer Function Call", "magenta", "on_grey"))

    yield Solution()

    print(colored("Teardown Outer Function Call", "magenta", "on_grey"))


@pytest.mark.usefixtures("resource")
class TestClass:
    # @classmethod
    # def setup_class(cls) -> None:
    #     print(colored(f"Setup Class : Start : class -> {cls.__name__} execution,green"))
    #     sol = Solution()

    # @classmethod
    # def teardown_class(cls) -> None:
    #     print(colored(f"Setup Class : Start : class -> {cls.__name__} execution,green"))

    def test_case_1(self, resource: resource) -> None:
        print(f"Testing : {resource}")
        sol = resource
        sol.lengthOfLongestSubstring("pwwkew")

    def test_case_2(self, resource: resource) -> None:
        print(f"Testing : {resource}")

        sol = resource
        assert sol.lengthOfLongestSubstring("abcdef") == 6

    def test_case_3(self, resource: resource) -> None:
        print(f"Testing : {resource}")

        sol = resource
        assert sol.lengthOfLongestSubstring("dvdf") == 3

    def test_case_4(self, resource: resource) -> None:
        print(f"Testing : {resource}")

        sol = resource
        assert sol.lengthOfLongestSubstring("abcabcbb") == 3

    def test_case_5(self, resource: resource) -> None:
        print(f"Testing : {resource}")

        sol = resource
        assert sol.lengthOfLongestSubstring("bbbbb") == 1

    def test_case_6(self, resource: resource) -> None:
        print(f"Testing : {resource}")

        sol = resource
        assert sol.lengthOfLongestSubstring("") == 0

    def test_case_7(self, resource: resource) -> None:
        print(f"Testing : {resource}")

        sol = resource
        assert sol.lengthOfLongestSubstring("dvdf") == 3

    def test_case_8(self, resource: resource) -> None:
        print(f"Testing : {resource}")

        sol = resource
        assert sol.lengthOfLongestSubstring("au") == 2

    def test_case_9(self, resource: resource) -> None:
        print(f"Testing : {resource}")

        sol = resource
        assert sol.lengthOfLongestSubstring("tmmzuxt") == 5

    def test_case_8(self, resource: resource) -> None:
        print(f"Testing : {resource}")

        sol = resource
        assert sol.lengthOfLongestSubstring("abba") == 2


def main() -> None:
    TestClass().test_case_1(Solution())


if __name__ == "__main__":
    pytest.main()
