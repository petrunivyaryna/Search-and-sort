"""Create a module using different methods of sorting and searching"""
import random
from typing import List
def linear_search(list_of_values, value):
    """
    lst, int -> int
    function return index of value in certain list
    >>> linear_search([1, 2, 3, 5], 4)
    -1
    >>> linear_search([8, 0 , 9, 9], 9)
    2
    """
    for i, elem in enumerate(list_of_values):
        if elem == value:
            return i
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

    if len(arr) == 0 or len(arr) == 1:
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
    low = 0
    last = len(list_of_values) - 1
    middle = 0
    while last >= low:
        middle = (low + last) // 2
        if list_of_values[middle] == value:
            return middle
        elif list_of_values[middle] < value:
            low = middle + 1
        else:
            last = middle-1
    return -1


def selection_sort(lst):
    """
    A function that sorts values in list using
    the selection sort algorithm.
    >>> selection_sort([19, 17, 3, 5, 2, 6, 10, 1])
    [1, 2, 3, 5, 6, 10, 17, 19]
    >>> selection_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5])
    [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9, 10]
    """
    def swap(list_1, elem1, elem2):
        first = list_1.pop(elem1)
        second = list_1.pop(elem2 - 1)
        list_1.insert(elem1, second)
        list_1.insert(elem2, first)
        return list_1
    for elem in range(len(lst)):
        min_element = elem
        for j in range(elem + 1, len(lst)):
            if lst[min_element] > lst[j]:
                min_element = j
        if min_element != elem:
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

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
    