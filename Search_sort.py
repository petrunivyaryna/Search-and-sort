import random
from typing import List
def linear_search(list_of_values, value):
    """
    lst, int -> int
    function return index of value in certain list
    >>> linear_search([1, 2, 3, 5], 4)
    -1
    >>> linear_search([num, 8, 0 , 9, 9], 9)
    3
    """
    for i, el in enumerate(list_of_values):
        if el == value:
            return i
    if value not in list_of_values:
        return -1
        
def merge_sort(arr: list) -> List[int]:
    '''
    Function to prform merge sort algorythm
    :param list arr: unsorted list
    :returns: sorted list
    :rtype: list
    >>> merge_sort([12, 11, 13, 5, 6, 7])
    [5, 6, 7, 11, 12, 13]
    '''
    def merge(left: list, right: list) -> list:
        '''
        Function to merge two lists into a sorted one
        :param list left: one of list to be merged
        :param list right: another list to be merged
        :returns: merged and sorted list
        :rtype: list
        >>> merge([1,5],[3,7])
        [1, 3, 5, 7]
        '''
        new_arr = []
        i = j = 0
        while len(new_arr) < len(left) + len(right):
            if left[i] > right[j]:
                new_arr.append(right[j])
                if right[j] != right[-1]:
                    j += 1
                else:
                    new_arr += left[i:]
            else:
                new_arr.append(left[i])
                if left[i] != left[-1]:
                    i += 1
                else:
                    new_arr += right[j:]
        return new_arr

    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = merge(left, right)
    return res

def binary_search(list_of_values, value):
    """
    lst, int --> int
    function return index of value in certain list
    >>> binary_search([2, 3, 4, 6, 7 ,9, 10], 8)
    -1
    >>> binary_search([2, 3, 4, 6, 7 ,9, 10], 6)
    3
    >>> binary_search([2, 3, 4, 6, 7 ,9, 12], 2)
    0
    """
    low = list_of_values[0]
    last = list_of_values[-1]
    while low <= last:
        middle = ((low + last)// 2)
        if value == middle:
            return list_of_values.index(middle)
        elif value > middle:
            low = middle +1
        elif value < middle:
            last = middle - 1
        return -1

def selection_sort(lst):
    """
    A function for sorting a list of values by selection method.
    >>> selection_sort([1, 4, 2, 5, 3, 6, 4, 7, 5, 8, 6])
    [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8]
    """
    def swap(list_1, elem1, elem2):
        list_1[elem1], list_1[elem2] = list_1[elem2], list_1[elem1]
        return list_1
    for elem in range(len(lst)):
        min_element = elem
        for j in range(elem, len(lst)):
            if lst[min_element] > lst[j]:
                min_element = j
            swap(lst, elem, min_element)
    return lst

def quick_sort(lst):
    """
    A function that sorts values in list using
    the quick sort algorithm.
    >>> quick_sort([1, 6, 2, 9, 3, 0, 4, 8, 3, 7, 3])
    [0, 1, 2, 3, 3, 3, 4, 6, 7, 8, 9]
    >>> quick_sort([1, 2, 56, 11, 2, 8, 38, 4, 8, 101])
    [1, 2, 2, 4, 8, 8, 11, 38, 56, 101]
    """
    if len(lst) <= 1:
        return lst
    rand_idx = random.randrange(len(lst))
    pivot = lst[rand_idx]
    smaller_numbers = [elem for i, elem in enumerate(lst) if elem <= pivot and i != rand_idx]
    biggest_numbers = [elem for i, elem in enumerate(lst) if elem > pivot]
    return quick_sort(smaller_numbers) + [pivot] + quick_sort(biggest_numbers)
    