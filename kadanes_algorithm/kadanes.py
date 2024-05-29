"""
This module implements Kadane's algorithm to find the maximum subarray sum.
"""

def simple_kadane(array:list[int]) -> int:
    """
    This function implements the Kadane's algorithm to find the maximum
    subarray sum in a given array.

    Parameters:
    array_intems (List[int]): The input array of integers.

    Returns:
    int: The maximum subarray sum.

    The function iterates through the array, maintaining two variables:
    max_so_far and max_ending_here.
    max_so_far keeps track of the maximum subarray sum found so far, while
    max_ending_here keeps track of the maximum subarray sum ending at the current position.
    At each iteration, the function updates max_ending_here by adding the current element to it.
    If max_ending_here becomes negative, it is reset to 0, as a new subarray sum
    must start from the next position.
    If max_so_far is less than max_ending_here, max_so_far is updated to max_ending_here.
    Finally, the function returns max_so_far, which represents the maximum subarray sum.
    """
    max_so_far = 0
    max_ending_here = 0
    for i in array:
        max_ending_here = max_ending_here + i
        # if max_ending_here < 0:
        #     max_ending_here = 0
        max_ending_here = max(max_ending_here, 0)
        # if max_so_far < max_ending_here:
        #     max_so_far = max_ending_here
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

if __name__ == "__main__":
    array_intems = [-1,2,-3,4,7,-5]
    final_ans = simple_kadane(array_intems)
    print(f"The maximum subarray sum is: {final_ans}")
