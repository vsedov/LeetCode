from K_Closest import Solution


def test_a():
    x = Solution()
    arr = [1, 1, 1, 10, 10, 10]
    point = x.findClosestElements(arr, 1, 9)
    assert point == [10]


def test_b():
    x = Solution()
    arr = [1, 2, 3, 4, 5]
    point = x.findClosestElements(arr, 4, 3)
    assert point == [1, 2, 3, 4]


def test_c():
    x = Solution()
    arr = [1, 2, 3, 4, 5]
    point = x.findClosestElements(arr, 4, -1)
    assert point == [1, 2, 3, 4]
