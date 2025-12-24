"""
Insertion Sort Exercise
=======================
Practice implementing insertion sort - intuitive and efficient for small/nearly sorted data!

Why Insertion Sort?
-------------------
Insertion sort works like sorting cards in your hand:
- Pick up cards one at a time
- Insert each card into its correct position among the cards you've already sorted

When to use it:
- Small arrays (often faster than O(n log n) algorithms due to low overhead)
- Nearly sorted data (best case is O(n)!)
- Online sorting (can sort as data arrives)
- As the base case for hybrid algorithms like Timsort

Visual Example:
    [5, 2, 4, 1, 3]
     ^              # 5 is "sorted" (first element)
    [5, 2, 4, 1, 3]
        ^           # Insert 2: shift 5 right, place 2
    [2, 5, 4, 1, 3]
           ^        # Insert 4: shift 5 right, place 4
    [2, 4, 5, 1, 3]
              ^     # Insert 1: shift 5,4,2 right, place 1
    [1, 2, 4, 5, 3]
                 ^  # Insert 3: shift 5,4 right, place 3
    [1, 2, 3, 4, 5]

Time Complexity:
- Best case: O(n) - already sorted!
- Average case: O(n²)
- Worst case: O(n²) - reverse sorted

Space Complexity: O(1) - truly in-place!

Instructions:
1. Implement each function according to its docstring
2. Run the file to check your solutions against the test cases
3. Start with basic insertion sort, then try the variations

Estimated time: 30 minutes
"""


# =============================================================================
# PROBLEM 1: Basic Insertion Sort
# =============================================================================


def insertion_sort(arr: list[int]) -> list[int]:
    """
    Sort a list using insertion sort algorithm.

    Algorithm:
    1. Start from index 1 (index 0 is trivially sorted)
    2. For each element at index i:
       a. Save the current element (key = arr[i])
       b. Compare with elements to the left (j = i - 1)
       c. Shift larger elements one position right
       d. Insert the key in its correct position
    3. Return the sorted list

    Think of it like sorting playing cards:
    - Your left hand holds the sorted cards
    - Your right hand picks up new cards one at a time
    - You insert each new card in the right place

    Examples:
        insertion_sort([5, 2, 4, 1, 3]) -> [1, 2, 3, 4, 5]
        insertion_sort([1, 2, 3]) -> [1, 2, 3]
        insertion_sort([3, 2, 1]) -> [1, 2, 3]
        insertion_sort([]) -> []
        insertion_sort([1]) -> [1]

    Args:
        arr: A list of integers to sort

    Returns:
        The sorted list (sorts in place but also returns it)
    """
    # TODO: Implement this function
    ...


# =============================================================================
# PROBLEM 2: Insertion Sort with Comparison Count
# =============================================================================


def insertion_sort_with_count(arr: list[int]) -> tuple[list[int], int]:
    """
    Insertion sort that counts comparisons made.

    This helps you see how insertion sort performs:
    - Best case (sorted): ~n comparisons
    - Worst case (reverse sorted): ~n²/2 comparisons

    A comparison is each time you compare two elements.

    Examples:
        insertion_sort_with_count([1, 2, 3]) -> ([1, 2, 3], 2)
            # Already sorted: just 2 comparisons to verify

        insertion_sort_with_count([3, 2, 1]) -> ([1, 2, 3], 3)
            # Reverse sorted: more comparisons needed

    Args:
        arr: A list of integers to sort

    Returns:
        Tuple of (sorted_list, comparison_count)
    """
    # TODO: Implement this function
    ...


# =============================================================================
# PROBLEM 3: Insertion Sort with Shift Count
# =============================================================================


def insertion_sort_with_shifts(arr: list[int]) -> tuple[list[int], int]:
    """
    Insertion sort that counts the number of shifts (moves) made.

    A shift is when you move an element one position to the right
    to make room for the key being inserted.

    This is useful because:
    - Each shift is a write operation (can be expensive)
    - Number of shifts = number of inversions in the array!

    Examples:
        insertion_sort_with_shifts([1, 2, 3]) -> ([1, 2, 3], 0)
            # No shifts needed - already sorted!

        insertion_sort_with_shifts([2, 1, 3]) -> ([1, 2, 3], 1)
            # One shift: move 2 right to insert 1

        insertion_sort_with_shifts([3, 2, 1]) -> ([1, 2, 3], 3)
            # Shifts: 3→, then 3→2→, total = 1 + 2 = 3

    Args:
        arr: A list of integers to sort

    Returns:
        Tuple of (sorted_list, shift_count)
    """
    # TODO: Implement this function
    ...


# =============================================================================
# PROBLEM 4: Binary Insertion Sort
# =============================================================================


def binary_insertion_sort(arr: list[int]) -> list[int]:
    """
    Insertion sort using binary search to find insertion position.

    Regular insertion sort does a linear search to find where to insert.
    This version uses binary search to find the position faster!

    Note: This reduces comparisons from O(n²) to O(n log n),
    BUT we still need O(n²) shifts in the worst case.
    So overall time complexity is still O(n²).

    Algorithm:
    1. For each element at index i (starting from 1):
       a. Use binary search to find correct position in arr[0:i]
       b. Shift elements right to make room
       c. Insert the element

    Examples:
        binary_insertion_sort([5, 2, 4, 1, 3]) -> [1, 2, 3, 4, 5]
        binary_insertion_sort([1, 2, 3]) -> [1, 2, 3]

    Args:
        arr: A list of integers to sort

    Returns:
        The sorted list
    """
    # TODO: Implement this function
    ...


# =============================================================================
# PROBLEM 5: Sort a Nearly Sorted Array
# =============================================================================


def sort_nearly_sorted(arr: list[int], k: int) -> list[int]:
    """
    Sort an array where each element is at most k positions away from its sorted position.

    This is where insertion sort SHINES! For nearly sorted data with small k,
    insertion sort runs in O(n*k) time, which is nearly linear when k is small.

    For example, if k=2, element at index 5 in the sorted array
    will be somewhere in indices 3-7 in the input array.

    Examples:
        sort_nearly_sorted([2, 1, 3, 4, 5], 1) -> [1, 2, 3, 4, 5]
            # Each element is at most 1 position away

        sort_nearly_sorted([3, 1, 2, 4], 2) -> [1, 2, 3, 4]
            # Each element is at most 2 positions away

    Hint: Regular insertion sort works great here! The inner loop
    will run at most k times for each element.

    Args:
        arr: A nearly sorted list where each element is at most k positions
             away from its final sorted position
        k: Maximum displacement of any element

    Returns:
        The sorted list
    """
    # TODO: Implement this function
    # Hint: You can use regular insertion sort - it's already optimal for this!
    ...


# =============================================================================
# TEST CASES - Run this file to test your implementations!
# =============================================================================


def test_insertion_sort():
    """Test the basic insertion_sort function."""
    print("\n" + "=" * 60)
    print("Testing: insertion_sort()")
    print("=" * 60)

    test_cases = [
        ([5, 2, 4, 1, 3], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([3, 3, 3], [3, 3, 3]),
        ([2, 1], [1, 2]),
        ([-5, -10, 0, 5, 10], [-10, -5, 0, 5, 10]),
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),
    ]

    passed = 0
    for arr, expected in test_cases:
        original = arr.copy()
        result = insertion_sort(arr.copy())
        status = "✓" if result == expected else "✗"
        if result == expected:
            passed += 1
        print(f"  {status} insertion_sort({original})")
        print(f"      Expected: {expected}")
        print(f"      Got:      {result}")

    print(f"\nPassed: {passed}/{len(test_cases)}")
    return passed == len(test_cases)


def test_insertion_sort_with_count():
    """Test insertion_sort_with_count function."""
    print("\n" + "=" * 60)
    print("Testing: insertion_sort_with_count()")
    print("=" * 60)

    test_cases = [
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([1], [1]),
        ([], []),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ]

    passed = 0
    for arr, expected_sorted in test_cases:
        original = arr.copy()
        result = insertion_sort_with_count(arr.copy())
        if result is None:
            print(f"  ✗ insertion_sort_with_count({original}) - returned None")
            continue

        sorted_result, count = result
        status = "✓" if sorted_result == expected_sorted else "✗"
        if sorted_result == expected_sorted:
            passed += 1
        print(f"  {status} insertion_sort_with_count({original})")
        print(f"      Sorted: {sorted_result}")
        print(f"      Comparisons: {count}")

    print(f"\nPassed: {passed}/{len(test_cases)}")
    return passed == len(test_cases)


def test_insertion_sort_with_shifts():
    """Test insertion_sort_with_shifts function."""
    print("\n" + "=" * 60)
    print("Testing: insertion_sort_with_shifts()")
    print("=" * 60)

    test_cases = [
        ([1, 2, 3], ([1, 2, 3], 0)),
        ([2, 1, 3], ([1, 2, 3], 1)),
        ([3, 2, 1], ([1, 2, 3], 3)),
        ([1], ([1], 0)),
        ([], ([], 0)),
        ([5, 4, 3, 2, 1], ([1, 2, 3, 4, 5], 10)),  # 1+2+3+4 = 10 shifts
    ]

    passed = 0
    for arr, (expected_sorted, expected_shifts) in test_cases:
        original = arr.copy()
        result = insertion_sort_with_shifts(arr.copy())
        if result is None:
            print(f"  ✗ insertion_sort_with_shifts({original}) - returned None")
            continue

        sorted_result, shift_count = result
        correct_sort = sorted_result == expected_sorted
        correct_shifts = shift_count == expected_shifts
        status = "✓" if correct_sort and correct_shifts else "✗"
        if correct_sort and correct_shifts:
            passed += 1
        print(f"  {status} insertion_sort_with_shifts({original})")
        print(f"      Sorted: {sorted_result} (expected {expected_sorted})")
        print(f"      Shifts: {shift_count} (expected {expected_shifts})")

    print(f"\nPassed: {passed}/{len(test_cases)}")
    return passed == len(test_cases)


def test_binary_insertion_sort():
    """Test binary_insertion_sort function."""
    print("\n" + "=" * 60)
    print("Testing: binary_insertion_sort()")
    print("=" * 60)

    test_cases = [
        ([5, 2, 4, 1, 3], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
    ]

    passed = 0
    for arr, expected in test_cases:
        original = arr.copy()
        result = binary_insertion_sort(arr.copy())
        status = "✓" if result == expected else "✗"
        if result == expected:
            passed += 1
        print(f"  {status} binary_insertion_sort({original})")
        print(f"      Expected: {expected}")
        print(f"      Got:      {result}")

    print(f"\nPassed: {passed}/{len(test_cases)}")
    return passed == len(test_cases)


def test_sort_nearly_sorted():
    """Test sort_nearly_sorted function."""
    print("\n" + "=" * 60)
    print("Testing: sort_nearly_sorted()")
    print("=" * 60)

    test_cases = [
        (([2, 1, 3, 4, 5], 1), [1, 2, 3, 4, 5]),
        (([3, 1, 2, 4], 2), [1, 2, 3, 4]),
        (([1, 2, 3], 0), [1, 2, 3]),
        (([6, 5, 3, 2, 8, 10, 9], 3), [2, 3, 5, 6, 8, 9, 10]),
        (([1], 0), [1]),
        (([], 0), []),
    ]

    passed = 0
    for (arr, k), expected in test_cases:
        original = arr.copy()
        result = sort_nearly_sorted(arr.copy(), k)
        status = "✓" if result == expected else "✗"
        if result == expected:
            passed += 1
        print(f"  {status} sort_nearly_sorted({original}, k={k})")
        print(f"      Expected: {expected}")
        print(f"      Got:      {result}")

    print(f"\nPassed: {passed}/{len(test_cases)}")
    return passed == len(test_cases)


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("INSERTION SORT EXERCISE - TEST RESULTS")
    print("=" * 60)

    results = {
        "insertion_sort": test_insertion_sort(),
        "insertion_sort_with_count": test_insertion_sort_with_count(),
        "insertion_sort_with_shifts": test_insertion_sort_with_shifts(),
        "binary_insertion_sort": test_binary_insertion_sort(),
        "sort_nearly_sorted": test_sort_nearly_sorted(),
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
        print("  • Insertion sort is O(n²) but O(n) for nearly sorted data")
        print("  • It's stable and in-place (O(1) extra space)")
        print("  • Great for small arrays or as part of hybrid algorithms")
        print("  • Binary search reduces comparisons but not shifts")
        print("  • Number of shifts = number of inversions!")
    else:
        print("\nKeep working on it! Tips:")
        print("  • Remember: start from index 1, not 0")
        print("  • The 'key' is the element being inserted")
        print("  • Shift elements right while they're greater than key")
        print("  • Think about sorting cards in your hand")

    return all_passed


if __name__ == "__main__":
    main()
