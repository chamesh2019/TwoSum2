# Two Sum II - Input Array is Sorted

A Python function to find two numbers in a sorted array that add up to a specific target.

## Problem Description

Given an array of integers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target. Return the indices of the two numbers (1-indexed) as an array.

## Usage

To find the indices of two numbers with a target sum, use the `two_sum` function. Example:

```python
from two_sum import two_sum

numbers = [2, 7, 11, 15]
target = 9
result = two_sum(numbers, target)
print(result)  # Output: [1, 2]

```
## Function Signature
```python
def two_sum(numbers, target):
    """
    Finds two numbers in a sorted array that add up to a specific target.

    Parameters:
    - `numbers`: A list of integers (sorted in non-decreasing order).
    - `target`: The target sum.

    Returns:
    - If a pair is found, returns the indices of the two numbers as a list [index1, index2].
    - If no pair is found, returns None.
    """
    # Implementation
```

## License
[MIT](https://choosealicense.com/licenses/mit/)