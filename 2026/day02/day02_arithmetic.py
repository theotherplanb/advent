"""
Solution for Advent of Code 2025 Day 02
using integer arithmetic instead of strings
"""

from functools import cache
from math import log10


@cache
def divisors(num_digits, part):
    """
    Return a list of divisors to check a product ID for repeated groups.

    Parameters:
        num_digits (int): The number of digits in the product ID
        part (int): The problem part (1 or 2) determining repetition rules

    Returns:
        list: List of divisors that can detect repeated digit groups

    An ID is invalid if it consists of a group of one or more digits
    repeated 2 or more times (exactly 2 for part 1). If this is the
    case then the number is an integer multiple of a "divisor" which
    has a 1 in the least-significant position of each group, and zeroes
    elsewhere. Examples: 777 == 11 * 7, 48314831 = 10001 * 4831
    """
    divisors_list = list()

    for num_groups in range(2, 3 if part == 1 else num_digits + 1):

        if num_digits % num_groups == 0:

            digits_per_group = num_digits // num_groups

            # Create divisor: sum of powers of 10 at each group position
            # For 3 groups of 2 digits: 10^0 + 10^2 + 10^4 = 1 + 100 + 10000 = 10101
            # Example: 156156156, 9 digits, 3 groups, divisor = 1001001
            # 156156156 / 1001001 == 156; 156156156 % 1001001 == 0
            divisors_list.append(sum(10 ** (digits_per_group * group)
                                 for group in range(num_groups)))
    return divisors_list


def sum_invalids(range_, part):
    """
    Calculate the sum of all the invalid product IDs in a range.

    Parameters:
        range_ (range): Range of product IDs to check
        part (int): The problem part (1 or 2) determining repetition rules

    Returns:
        int: Sum of all invalid product IDs in the given range
    """
    total = 0
    for pid in range_:

        # Calculate number of digits: log10(n) + 1 (e.g., log10(1234) = 3.09, so 4 digits)
        for divisor in divisors(int(log10(pid)) + 1, part):

            if pid % divisor == 0:

                total += pid

                break
    return total


with open('input', 'r') as f:
    input_data = f.read().strip().split(',')

range_pairs = [range_.split('-') for range_ in input_data]
ranges = [range(int(fr), int(to) + 1) for fr, to in range_pairs]



for part in (1, 2):
    print(f'Part {part}: {sum([sum_invalids(range_, part) for range_ in ranges])}')
