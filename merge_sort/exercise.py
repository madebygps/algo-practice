"""
Merge Sort Exercise
===================
Practice implementing merge sort - an O(n log n) divide-and-conquer algorithm!

Why Merge Sort?
---------------
Merge sort is a classic divide-and-conquer algorithm that:
- Always runs in O(n log n) time (worst, average, and best case!)
- Is stable (preserves relative order of equal elements)
- Is great for sorting linked lists and external sorting

How it works:
1. DIVIDE: Split the array in half recursively until you have single elements
2. CONQUER: Merge the sorted halves back together

Visual Example:
    [38, 27, 43, 3]
         /     \
    [38, 27]  [43, 3]      <- Split
      /  \      /  \
    [38] [27] [43] [3]     <- Single elements (base case)
      \  /      \  /
    [27, 38]  [3, 43]      <- Merge sorted halves
         \     /
    [3, 27, 38, 43]        <- Final merge

Time Complexity: O(n log n)
- We divide the array log(n) times
- Each level requires O(n) work to merge

Space Complexity: O(n)
- We need extra space for the temporary arrays during merging

Instructions:
1. Implement each function according to its docstring
2. Run the file to check your solutions against the test cases
3. Start with the merge function - it's the key building block!

Estimated time: 45 minutes
"""


# =============================================================================
# PROBLEM 1: Merge Two Sorted Lists
# =============================================================================


def merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merge two sorted lists into one sorted list.

    This is the KEY operation in merge sort! Understanding this function
    is essential before implementing the full algorithm.

    Algorithm:
    1. Create an empty result list
    2. Use two pointers (i for left, j for right), both starting at 0
    3. While both lists have elements remaining:
       a. Compare left[i] and right[j]
       b. Append the smaller one to result
       c. Move that pointer forward
    4. Append any remaining elements from either list
    5. Return result

    Examples:
        merge([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
        merge([1, 2], [3, 4]) -> [1, 2, 3, 4]
        merge([5, 10], [1, 2, 3]) -> [1, 2, 3, 5, 10]
        merge([], [1, 2]) -> [1, 2]
        merge([1], []) -> [1]

    Args:
        left: A sorted list of integers
        right: A sorted list of integers

    Returns:
        A new sorted list containing all elements from both lists
    """
    i = 0
    j = 0
    final = []
    while i < len(left) and j < len(right):
        if left[i] <= right [j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1
    while i < len(left):
        final.append(left[i])
        i += 1
    while j < len(right):
        final.append(right[j])
        j += 1

    return final



# =============================================================================
# PROBLEM 2: Basic Merge Sort
# =============================================================================


def merge_sort(arr: list[int]) -> list[int]:
    """
    Sort a list using the merge sort algorithm.

    Algorithm (recursive):
    1. BASE CASE: If list has 0 or 1 elements, it's already sorted - return it
    2. DIVIDE: Split the list into two halves
       - mid = len(arr) // 2
       - left_half = arr[:mid]
       - right_half = arr[mid:]
    3. CONQUER: Recursively sort each half
       - sorted_left = merge_sort(left_half)
       - sorted_right = merge_sort(right_half)
    4. COMBINE: Merge the sorted halves using your merge function
       - return merge(sorted_left, sorted_right)

    Examples:
        merge_sort([38, 27, 43, 3, 9, 82, 10]) -> [3, 9, 10, 27, 38, 43, 82]
        merge_sort([5, 4, 3, 2, 1]) -> [1, 2, 3, 4, 5]
        merge_sort([1]) -> [1]
        merge_sort([]) -> []
        merge_sort([3, 3, 3]) -> [3, 3, 3]

    Args:
        arr: A list of integers to sort

    Returns:
        A new sorted list (does not modify the original)
    """
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left_sorted = merge_sort(arr[:mid])
    right_sorted = merge_sort(arr[mid:])

    return(merge(left_sorted, right_sorted))


# =============================================================================
# PROBLEM 3: Merge Sort with Step Counter
# =============================================================================


def merge_sort_with_count(arr: list[int]) -> tuple[list[int], int]:
    """
    Merge sort that counts the number of comparisons made.

    This helps you verify that merge sort is O(n log n)!
    A comparison happens each time you compare two elements during merging.

    Hint: You'll need to modify both merge and merge_sort to pass
    the count around. Consider using a helper function.

    Examples:
        merge_sort_with_count([3, 1, 2]) -> ([1, 2, 3], 3)
            # Comparisons: 1 vs 3, 2 vs 3, 2 vs 1 (approximately)

        merge_sort_with_count([1]) -> ([1], 0)
            # No comparisons needed for single element

    Args:
        arr: A list of integers to sort

    Returns:
        Tuple of (sorted_list, comparison_count)
    """
    # TODO: Implement this function
    pass


# =============================================================================
# PROBLEM 4: In-Place-ish Merge Sort (Challenge!)
# =============================================================================


def merge_sort_in_place(arr: list[int]) -> None:
    """
    Sort a list in-place using merge sort.

    Note: True in-place merge sort is complex. This version can use
    O(n) extra space during merging but should modify the original list
    rather than returning a new one.

    This is how you'd typically use merge sort in practice when you
    want to modify the original list.

    Examples:
        arr = [38, 27, 43, 3]
        merge_sort_in_place(arr)
        # arr is now [3, 27, 38, 43]

        arr = [5, 4, 3, 2, 1]
        merge_sort_in_place(arr)
        # arr is now [1, 2, 3, 4, 5]

    Args:
        arr: A list of integers to sort (modified in place)

    Returns:
        None (modifies arr in place)
    """
    # TODO: Implement this function
    pass


# =============================================================================
# PROBLEM 5: Count Inversions (Classic Application!)
# =============================================================================


def count_inversions(arr: list[int]) -> int:
    """
    Count the number of inversions in an array using merge sort.

    An inversion is a pair (i, j) where i < j but arr[i] > arr[j].
    This is a classic application of merge sort!

    Why merge sort? During the merge step, when we take an element from
    the right array, all remaining elements in the left array form
    inversions with it!

    Examples:
        count_inversions([1, 2, 3]) -> 0
            # Already sorted, no inversions

        count_inversions([3, 2, 1]) -> 3
            # Inversions: (3,2), (3,1), (2,1)

        count_inversions([1, 3, 2]) -> 1
            # Inversion: (3,2)

        count_inversions([2, 4, 1, 3, 5]) -> 3
            # Inversions: (2,1), (4,1), (4,3)

    Args:
        arr: A list of integers

    Returns:
        The number of inversions in the array
    """
    # TODO: Implement this function
    pass


# =============================================================================
# TEST CASES - Run this file to test your implementations!
# =============================================================================


def test_merge():
    """Test the merge function."""
    print("\n" + "=" * 60)
    print("Testing: merge()")
    print("=" * 60)

    test_cases = [
        (([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]),
        (([1, 2], [3, 4]), [1, 2, 3, 4]),
        (([3, 4], [1, 2]), [1, 2, 3, 4]),
        (([5, 10], [1, 2, 3]), [1, 2, 3, 5, 10]),
        (([], [1, 2]), [1, 2]),
        (([1], []), [1]),
        (([], []), []),
        (([1, 1, 1], [1, 1]), [1, 1, 1, 1, 1]),
        (([1, 5, 9], [2, 6, 10]), [1, 2, 5, 6, 9, 10]),
    ]

    passed = 0
    for (left, right), expected in test_cases:
        result = merge(left, right)
        status = "✓" if result == expected else "✗"
        if result == expected:
            passed += 1
        print(f"  {status} merge({left}, {right})")
        print(f"      Expected: {expected}")
        print(f"      Got:      {result}")

    print(f"\nPassed: {passed}/{len(test_cases)}")
    return passed == len(test_cases)


def test_merge_sort():
    """Test the merge_sort function."""
    print("\n" + "=" * 60)
    print("Testing: merge_sort()")
    print("=" * 60)

    test_cases = [
        ([38, 27, 43, 3, 9, 82, 10], [3, 9, 10, 27, 38, 43, 82]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([3, 3, 3], [3, 3, 3]),
        ([2, 1], [1, 2]),
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
        ([-5, -10, 0, 5, 10], [-10, -5, 0, 5, 10]),
        ([1, 0, -1, 2, -2], [-2, -1, 0, 1, 2]),
    ]

    passed = 0
    for arr, expected in test_cases:
        original = arr.copy()
        result = merge_sort(arr)
        status = "✓" if result == expected else "✗"
        if result == expected:
            passed += 1
        print(f"  {status} merge_sort({original})")
        print(f"      Expected: {expected}")
        print(f"      Got:      {result}")

    print(f"\nPassed: {passed}/{len(test_cases)}")
    return passed == len(test_cases)


def test_merge_sort_with_count():
    """Test the merge_sort_with_count function."""
    print("\n" + "=" * 60)
    print("Testing: merge_sort_with_count()")
    print("=" * 60)

    test_cases = [
        ([1], ([1], 0)),
        ([], ([], 0)),
        ([2, 1], ([1, 2], 1)),
        ([1, 2], ([1, 2], 1)),
    ]

    passed = 0
    for arr, (expected_sorted, _) in test_cases:
        original = arr.copy()
        result = merge_sort_with_count(arr)
        if result is None:
            print(f"  ✗ merge_sort_with_count({original}) - returned None")
            continue

        sorted_result, count = result
        # We mainly check the sorted result; count can vary by implementation
        status = "✓" if sorted_result == expected_sorted else "✗"
        if sorted_result == expected_sorted:
            passed += 1
        print(f"  {status} merge_sort_with_count({original})")
        print(f"      Sorted:      {sorted_result} (expected {expected_sorted})")
        print(f"      Comparisons: {count}")

    # Additional test to verify count is reasonable (n log n)
    large_arr = list(range(100, 0, -1))  # Reversed list of 100 elements
    result = merge_sort_with_count(large_arr)
    if result:
        sorted_result, count = result
        is_sorted = sorted_result == list(range(1, 101))
        # For n=100, n*log2(n) ≈ 665, actual comparisons should be less
        reasonable_count = count < 1000
        if is_sorted and reasonable_count:
            passed += 1
            print(f"  ✓ Large array (100 elements): {count} comparisons")
        else:
            print(f"  ✗ Large array: sorted={is_sorted}, count={count}")

    print(f"\nPassed: {passed}/{len(test_cases) + 1}")
    return passed == len(test_cases) + 1


def test_merge_sort_in_place():
    """Test the merge_sort_in_place function."""
    print("\n" + "=" * 60)
    print("Testing: merge_sort_in_place()")
    print("=" * 60)

    test_cases = [
        ([38, 27, 43, 3], [3, 27, 38, 43]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
    ]

    passed = 0
    for arr, expected in test_cases:
        original = arr.copy()
        test_arr = arr.copy()
        merge_sort_in_place(test_arr)
        status = "✓" if test_arr == expected else "✗"
        if test_arr == expected:
            passed += 1
        print(f"  {status} merge_sort_in_place({original})")
        print(f"      Expected: {expected}")
        print(f"      Got:      {test_arr}")

    print(f"\nPassed: {passed}/{len(test_cases)}")
    return passed == len(test_cases)


def test_count_inversions():
    """Test the count_inversions function."""
    print("\n" + "=" * 60)
    print("Testing: count_inversions()")
    print("=" * 60)

    test_cases = [
        ([1, 2, 3], 0),
        ([3, 2, 1], 3),
        ([1, 3, 2], 1),
        ([2, 4, 1, 3, 5], 3),
        ([1], 0),
        ([], 0),
        ([2, 1], 1),
        ([5, 4, 3, 2, 1], 10),  # 4+3+2+1 = 10 inversions
        ([1, 1, 1], 0),
    ]

    passed = 0
    for arr, expected in test_cases:
        result = count_inversions(arr)
        status = "✓" if result == expected else "✗"
        if result == expected:
            passed += 1
        print(f"  {status} count_inversions({arr})")
        print(f"      Expected: {expected}")
        print(f"      Got:      {result}")

    print(f"\nPassed: {passed}/{len(test_cases)}")
    return passed == len(test_cases)


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("MERGE SORT EXERCISE - TEST RESULTS")
    print("=" * 60)

    results = {
        "merge": test_merge(),
        "merge_sort": test_merge_sort(),
        # "merge_sort_with_count": test_merge_sort_with_count(),
        # "merge_sort_in_place": test_merge_sort_in_place(),
        # "count_inversions": test_count_inversions(),
    }

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    all_passed = True
    for name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"  {status}: {name}")
        if not passed:
            all_passed = False

    if all_passed:
        print("\n🎉 Congratulations! All tests passed!")
        print("\nKey takeaways:")
        print("  • Merge sort divides the problem in half recursively")
        print("  • The merge operation is O(n) and is the key building block")
        print("  • Total time complexity: O(n log n) - always!")
        print("  • Space complexity: O(n) for the temporary arrays")
        print("  • Counting inversions is a classic merge sort application")
    else:
        print("\nKeep working on it! Tips:")
        print("  • Start with merge() - it's the foundation")
        print("  • Draw out the recursive calls on paper")
        print("  • Remember the base case: arrays of 0 or 1 element")

    return all_passed


if __name__ == "__main__":
    main()
