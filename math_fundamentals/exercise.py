"""
Math Fundamentals Exercise
==========================
Practice problems covering: Exponents, Logarithms, Factorials, and Averages

Instructions:
1. Implement each function according to its docstring
2. Run the file to check your solutions against the test cases
3. Don't use built-in functions like math.factorial() - implement the logic yourself!

Estimated time: 30 minutes
"""

import math


# =============================================================================
# PROBLEM 1: Exponents
# =============================================================================

def power(base: int, exponent: int) -> int:
    """
    Calculate base raised to the power of exponent WITHOUT using ** or pow().
    
    Use a loop to multiply base by itself exponent times.
    
    Examples:
        power(2, 3) -> 8      (2 * 2 * 2)
        power(5, 0) -> 1      (anything to the 0 is 1)
        power(3, 4) -> 81     (3 * 3 * 3 * 3)
    
    Args:
        base: The base number
        exponent: The power to raise base to (non-negative integer)
    
    Returns:
        base raised to the exponent
    """
    # TODO: Implement this function
    total = 1
    for n in range(exponent):
        total *= base
    return total


# =============================================================================
# PROBLEM 2: Factorial
# =============================================================================

def factorial(n: int) -> int:
    """
    Calculate n! (n factorial) WITHOUT using math.factorial().
    
    Factorial is the product of all positive integers up to n.
    n! = n * (n-1) * (n-2) * ... * 2 * 1
    
    Examples:
        factorial(0) -> 1     (by definition)
        factorial(1) -> 1
        factorial(5) -> 120   (5 * 4 * 3 * 2 * 1)
        factorial(7) -> 5040
    
    Args:
        n: A non-negative integer
    
    Returns:
        The factorial of n
    """
    # TODO: Implement this function
    total = 1

    for n in range(1, n + 1):
        total *= n
    return total

    pass


# =============================================================================
# PROBLEM 3: Logarithm (Integer floor of log base 2)
# =============================================================================

def log_base_2(n: int) -> int:
    """
    Calculate the floor of log base 2 of n WITHOUT using math.log().
    
    This is essentially asking: "How many times can I divide n by 2 before 
    reaching 1?" This is crucial for understanding O(log n) complexity!
    
    Hint: Keep dividing n by 2 until n becomes 1, counting iterations.
    
    Examples:
        log_base_2(1) -> 0    (2^0 = 1)
        log_base_2(2) -> 1    (2^1 = 2)
        log_base_2(8) -> 3    (2^3 = 8)
        log_base_2(10) -> 3   (2^3 = 8 <= 10 < 16 = 2^4)
        log_base_2(16) -> 4   (2^4 = 16)
    
    Args:
        n: A positive integer
    
    Returns:
        Floor of log base 2 of n

    """

    total = 2
    total_times = 0

    if n == 1:
        return 0
    else:
        while total <= n:
                total *= 2
                total_times += 1
        return total_times

    
# =============================================================================
# PROBLEM 4: Average (Mean)
# =============================================================================

def average(numbers: list[float]) -> float:
    """
    Calculate the average (arithmetic mean) of a list of numbers.
    
    Average = sum of all numbers / count of numbers
    
    Examples:
        average([1, 2, 3, 4, 5]) -> 3.0
        average([10, 20]) -> 15.0
        average([7]) -> 7.0
    
    Args:
        numbers: A non-empty list of numbers
    
    Returns:
        The arithmetic mean of the numbers
    """
    # TODO: Implement this function

    average = 0

    for n in numbers:
        average+=n
    
    return average/len(numbers)
    pass


# =============================================================================
# TEST CASES - Run this file to check your solutions!
# =============================================================================

def run_tests():
    print("=" * 60)
    print("MATH FUNDAMENTALS - TEST RESULTS")
    print("=" * 60)
    
    all_passed = True
    
    # Test power()
    print("\n📊 Testing power()...")
    power_tests = [
        ((2, 3), 8),
        ((5, 0), 1),
        ((3, 4), 81),
        ((2, 10), 1024),
        ((10, 2), 100),
    ]
    for (base, exp), expected in power_tests:
        result = power(base, exp)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_passed = False
        print(f"  {status} power({base}, {exp}) = {result} (expected {expected})")
    
    # Test factorial()
    print("\n🔢 Testing factorial()...")
    factorial_tests = [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040),
        (10, 3628800),
    ]
    for n, expected in factorial_tests:
        result = factorial(n)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_passed = False
        print(f"  {status} factorial({n}) = {result} (expected {expected})")
    
    # Test log_base_2()
    print("\n📈 Testing log_base_2()...")
    log_tests = [
        (1, 0),
        (2, 1),
        (8, 3),
        (10, 3),
        (16, 4),
        (100, 6),
    ]
    for n, expected in log_tests:
        result = log_base_2(n)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_passed = False
        print(f"  {status} log_base_2({n}) = {result} (expected {expected})")
    
    # Test average()
    print("\n📉 Testing average()...")
    average_tests = [
        ([1, 2, 3, 4, 5], 3.0),
        ([10, 20], 15.0),
        ([7], 7.0),
        ([1, 1, 1, 1], 1.0),
        ([0, 10], 5.0),
    ]
    for nums, expected in average_tests:
        result = average(nums)
        status = "✅" if result == expected else "❌"
        if result != expected:
            all_passed = False
        print(f"  {status} average({nums}) = {result} (expected {expected})")
    
  
    
    # Summary
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ALL TESTS PASSED! Great job!")
    else:
        print("💪 Some tests failed. Keep trying!")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
