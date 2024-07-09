#!/usr/bin/python3
"""
Module for finding a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    A peak element is an element that is greater than its neighbors.
    For the elements at the boundaries, we only need to consider one neighbor.
    
    Args:
        list_of_integers (list): List of unsorted integers.
        
    Returns:
        int: A peak element, or None if the list is empty.
    """
    if not list_of_integers:
        return None
    
    def find_peak_recursive(nums, left, right):
        """
        Helper function to find a peak using a binary search approach.
        """
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            return find_peak_recursive(nums, mid + 1, right)
        else:
            return find_peak_recursive(nums, left, mid)
    
    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)

