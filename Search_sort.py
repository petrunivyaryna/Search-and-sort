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
    """
    pass