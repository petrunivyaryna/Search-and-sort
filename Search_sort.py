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
    """
    pass

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