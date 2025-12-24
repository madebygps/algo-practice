"""
Merge Sort Exercise (~20 min)
=============================
Divide-and-conquer: split in half, sort each half, merge back together.

    [38, 27, 43, 3]  →  [38, 27] [43, 3]  →  [38] [27] [43] [3]
                                          ↓
    [3, 27, 38, 43]  ←  [27, 38] [3, 43]  ←  merge sorted halves

Time: O(n log n) | Space: O(n)
"""


def merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merge two sorted lists into one sorted list.

    Hint: Use two pointers, compare elements, take the smaller one.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    """
    # TODO: Implement
    pass


def merge_sort(arr: list[int]) -> list[int]:
    """
    Sort using merge sort.

    Hint: Base case (len < 2), split in half, recurse, merge.

    >>> merge_sort([38, 27, 43, 3])
    [3, 27, 38, 43]
    """
    # TODO: Implement
    pass


# =============================================================================
# TESTS
# =============================================================================
if __name__ == "__main__":
    # Test merge
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert merge([], [1, 2]) == [1, 2]
    assert merge([1], []) == [1]
    print("✓ merge")

    # Test merge_sort
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([1]) == [1]
    assert merge_sort([]) == []
    print("✓ merge_sort")

    print("\n🎉 All tests passed!")
