def two_sum(numbers, target):
    """
    Given a list of numbers and a target value, finds two numbers in the list that add up to the target value and returns their indices.
    
    Parameters:
        - numbers (list): A list of numbers.
        - target (int): The target value.
        
    Returns:
        - list: A list containing the indices of the two numbers that add up to the target value.
    """
    left, right = 0, len(numbers) - 1
 
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]
        
        if current_sum > target:
            right -= 1
        
        if current_sum < target:
            left += 1
    
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))