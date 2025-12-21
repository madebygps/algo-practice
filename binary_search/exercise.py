"""
Binary Search Exercise
======================
Practice implementing binary search - an O(log n) algorithm!

Why Binary Search?
------------------
Remember log_base_2 from the math exercise? Binary search is WHY that matters!
- Linear search: O(n) - check every element
- Binary search: O(log n) - eliminate half the elements each step

For a sorted list of 1,000,000 elements:
- Linear search: up to 1,000,000 comparisons
- Binary search: at most 20 comparisons! (log₂(1,000,000) ≈ 20)

Prerequisites:
- The list MUST be sorted
- You need to be able to access elements by index

Instructions:
1. Implement each function according to its docstring
2. Run the file to check your solutions against the test cases
3. Try to understand the pattern: divide the search space in half each time

Estimated time: 30 minutes
"""


# =============================================================================
# PROBLEM 1: Basic Binary Search
# =============================================================================


def binary_search(sorted_list: list[int], target: int) -> int:
    """
    Find the index of target in a sorted list using binary search.

    Algorithm:
    1. Set left pointer to start (0) and right pointer to end (len-1)
    2. While left <= right:
       a. Find the middle index: mid = (left + right) // 2
       b. If sorted_list[mid] == target: return mid (found it!)
       c. If sorted_list[mid] < target: search right half (left = mid + 1)
       d. If sorted_list[mid] > target: search left half (right = mid - 1)
    3. If loop ends without finding, return -1

    Examples:
        binary_search([1, 3, 5, 7, 9], 5) -> 2
        binary_search([1, 3, 5, 7, 9], 1) -> 0
        binary_search([1, 3, 5, 7, 9], 9) -> 4
        binary_search([1, 3, 5, 7, 9], 4) -> -1 (not found)

    Args:
        sorted_list: A list of integers sorted in ascending order
        target: The value to search for

    Returns:
        Index of target if found, -1 if not found
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# =============================================================================
# PROBLEM 2: Count Comparisons
# =============================================================================


def binary_search_with_count(sorted_list: list[int], target: int) -> tuple[int, int]:
    """
    Same as binary_search, but also count how many comparisons were made.

    This helps you see WHY binary search is O(log n) - the number of
    comparisons should be roughly log₂(n)!

    A "comparison" is each time you check if sorted_list[mid] equals,
    is less than, or greater than the target.

    Examples:
        binary_search_with_count([1, 3, 5, 7, 9], 5) -> (2, 1)
            # Found at index 2, took 1 comparison (hit middle first try)

        binary_search_with_count([1, 2, 3, 4, 5, 6, 7, 8], 1) -> (0, 3)
            # Found at index 0, took 3 comparisons

    Args:
        sorted_list: A list of integers sorted in ascending order
        target: The value to search for

    Returns:
        Tuple of (index, comparison_count)
        Index is -1 if not found
    """
    low = 0
    high = len(sorted_list) - 1
    comparison_count = 0

    while low <= high:
        mid = (high + low) // 2
        if sorted_list[mid] == target:
            comparison_count += 1
            return (mid, comparison_count)
        elif sorted_list[mid] < target:
            low = mid + 1
            comparison_count += 1
        else:
            high = mid - 1
            comparison_count += 1
    return (-1, comparison_count)


# =============================================================================
# PROBLEM 3: Find First Occurrence
# =============================================================================


def binary_search_first(sorted_list: list[int], target: int) -> int:
    """
    Find the FIRST occurrence of target in a sorted list that may have duplicates.

    Regular binary search might find ANY occurrence. This version finds
    the leftmost (first) one.

    Hint: When you find the target, don't return immediately!
    Instead, record it and keep searching LEFT to see if there's an earlier one.

    Examples:
        binary_search_first([1, 2, 2, 2, 3], 2) -> 1  (first 2 is at index 1)
        binary_search_first([1, 1, 1, 1, 1], 1) -> 0  (first 1 is at index 0)
        binary_search_first([1, 2, 3, 4, 5], 3) -> 2  (only one 3)
        binary_search_first([1, 2, 3], 5) -> -1       (not found)

    Args:
        sorted_list: A sorted list that may contain duplicates
        target: The value to search for

    Returns:
        Index of the FIRST occurrence of target, or -1 if not found
    """
    low = 0
    high = len(sorted_list) - 1

    first_index = -1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            first_index = mid
            high = mid - 1
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first_index


# =============================================================================
# PROBLEM 4: Find Insert Position
# =============================================================================


def find_insert_position(sorted_list: list[int], target: int) -> int:
    """
    Find the index where target should be inserted to keep the list sorted.

    If target already exists, return the index of the existing element.
    This is useful for maintaining sorted data structures!

    Examples:
        find_insert_position([1, 2, 3, 5, 7], 4) -> 2  (insert between 3 and 5)
        find_insert_position([1, 3, 5, 7], 0) -> 0  (insert at beginning)
        find_insert_position([1, 3, 5, 7], 8) -> 4  (insert at end)
        find_insert_position([1, 3, 5, 7], 5) -> 2  (5 already exists at index 2)

    Args:
        sorted_list: A list of integers sorted in ascending order
        target: The value to find insert position for

    Returns:
        Index where target should be inserted
    """

    low = 0
    high = len(sorted_list) - 1 #3


    while low <= high:
        mid = (low + high) // 2 #1 -- 
        if sorted_list[mid] == target: # 3==0?
            return mid
        elif sorted_list[mid] < target:#3<0
            low = mid + 1
        else:
            high = mid - 1 #0
    return low


# =============================================================================
# PROBLEM 5: Square Root (BONUS - Binary Search on Answer!)
# =============================================================================


def integer_sqrt(n: int) -> int:
    """
    Find the integer square root of n using binary search.

    The integer square root is the largest integer x where x*x <= n.

    This shows binary search isn't just for finding items in a list -
    you can use it to search for ANY value in a sorted range!

    Think of it as: "search for the answer between 0 and n"

    Examples:
        integer_sqrt(16) -> 4   (4*4 = 16)
        integer_sqrt(15) -> 3   (3*3 = 9 <= 15 < 16 = 4*4)
        integer_sqrt(26) -> 5   (5*5 = 25 <= 26 < 36 = 6*6)
        integer_sqrt(1) -> 1
        integer_sqrt(0) -> 0

    Args:
        n: A non-negative integer

    Returns:
        The largest integer x where x*x <= n
    """
    # TODO: Use binary search to find the square root
    # Hint: Search between 0 and n, check if mid*mid <= n

    low = 0
    high = n
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if mid*mid <= n:
            result = mid
            low = mid + 1
        else:
            high = mid - 1 
    return result


# =============================================================================
# TEST CASES - Run this file to check your solutions!
# =============================================================================


def run_tests():
    print("=" * 60)
    print("BINARY SEARCH - TEST RESULTS")
    print("=" * 60)

    all_passed = True

    # Test binary_search()
    print("\n🔍 Testing binary_search()...")
    search_tests = [
        (([1, 3, 5, 7, 9], 5), 2),
        (([1, 3, 5, 7, 9], 1), 0),
        (([1, 3, 5, 7, 9], 9), 4),
        (([1, 3, 5, 7, 9], 4), -1),
        (([1, 3, 5, 7, 9], 0), -1),
        (([], 5), -1),
        (([42], 42), 0),
    ]
    for (lst, target), expected in search_tests:
        result = binary_search(lst, target)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_passed = False
        print(
            f"  {status} binary_search({lst}, {target}) = {result} (expected {expected})"
        )

    # Test binary_search_with_count()
    print("\n📊 Testing binary_search_with_count()...")
    count_tests = [
        (([1, 3, 5, 7, 9], 5), 2),  # Just check index, comparisons vary
        (([1, 2, 3, 4, 5, 6, 7, 8], 1), 0),
    ]
    for (lst, target), expected_idx in count_tests:
        result = binary_search_with_count(lst, target)
        if result is None:
            status = "❌"
            all_passed = False
            print(
                f"  {status} binary_search_with_count({lst}, {target}) = None (not implemented)"
            )
        else:
            idx, count = result
            status = "✅" if idx == expected_idx else "❌"
            if idx != expected_idx:
                all_passed = False
            print(
                f"  {status} binary_search_with_count({lst}, {target}) = index {idx}, {count} comparisons"
            )

    # Demonstrate O(log n)
    big_list = list(range(1000000))
    result = binary_search_with_count(big_list, 1)
    if result:
        idx, count = result
        print(
            f"  📈 Searching 1,000,000 elements took only {count} comparisons! (log₂(1000000) ≈ 20)"
        )

    # Test binary_search_first()
    print("\n1️⃣ Testing binary_search_first()...")
    first_tests = [
        (([1, 2, 2, 2, 3], 2), 1),
        (([1, 1, 1, 1, 1], 1), 0),
        (([1, 2, 3, 4, 5], 3), 2),
        (([1, 2, 3], 5), -1),
        (([2, 2, 2, 2, 2], 2), 0),
    ]
    for (lst, target), expected in first_tests:
        result = binary_search_first(lst, target)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_passed = False
        print(
            f"  {status} binary_search_first({lst}, {target}) = {result} (expected {expected})"
        )

    # Test find_insert_position()
    print("\n📍 Testing find_insert_position()...")
    insert_tests = [
        (([1, 3, 5, 7], 4), 2),
        (([1, 3, 5, 7], 0), 0),
        (([1, 3, 5, 7], 8), 4),
        (([1, 3, 5, 7], 5), 2),
        (([], 5), 0),
    ]
    for (lst, target), expected in insert_tests:
        result = find_insert_position(lst, target)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_passed = False
        print(
            f"  {status} find_insert_position({lst}, {target}) = {result} (expected {expected})"
        )

    # Test integer_sqrt()
    print("\n√ Testing integer_sqrt()...")
    sqrt_tests = [
        (16, 4),
        (15, 3),
        (26, 5),
        (1, 1),
        (0, 0),
        (100, 10),
        (99, 9),
    ]
    for n, expected in sqrt_tests:
        result = integer_sqrt(n)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_passed = False
        print(f"  {status} integer_sqrt({n}) = {result} (expected {expected})")

    # Summary
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ALL TESTS PASSED! You've mastered binary search!")
    else:
        print("💪 Some tests failed. Keep trying!")
    print("=" * 60)

    # Educational note
    print("\n📚 Remember: Binary search is O(log n) because you")
    print("   eliminate HALF the remaining elements each step!")
    print("   This is why log₂ matters in algorithm analysis.")


if __name__ == "__main__":
    run_tests()
