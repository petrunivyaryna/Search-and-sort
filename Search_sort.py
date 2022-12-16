import random
def linear_search(list_of_values, value):
    """
    """
    pass

def merge_sort(lst):
    """
    """
    pass

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
    >>> selection_sort([1,4,2,5,3,6,4,7,5,8,6])
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
    