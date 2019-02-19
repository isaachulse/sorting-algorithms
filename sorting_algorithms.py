#!/usr/bin/python
import sys

################################################################################
##                                                                            ##
##  PYTHON  3 IMPLEMENTATION OF BUBBLE SORT, QUICK SORT AND SELECTION SORT    ##
##                                                                            ##
################################################################################

def convert_list(mixed_list):
    list_len = len(mixed_list)
    unsorted_list = []
    for i in range(list_len):
        if isinstance(mixed_list[i], int) or isinstance(mixed_list[i], float):
            unsorted_list.append(mixed_list[i])
        elif isinstance(mixed_list[i], str):
            try:
                unsorted_list.append(float(mixed_list[i]))
            except ValueError:
                unsorted_list.append(None)
        else:
            unsorted_list.append(None)
    unsorted_list = [x for x in unsorted_list if x != None]
    return unsorted_list

def bubble_sort(mixed_list):
    unsorted_list = convert_list(mixed_list)
    list_len = len(unsorted_list)
    if list_len <= 1:
        sorted_list = unsorted_list
        return sorted_list
    else:
        for i in range(list_len):
            for j in range(list_len - 1):
                if unsorted_list[j] > unsorted_list[j + 1]:
                    tmp = unsorted_list[j]
                    unsorted_list[j] = unsorted_list[j + 1]
                    unsorted_list[j + 1] = tmp
        sorted_list = unsorted_list
    return sorted_list


def quick_sort(mixed_list):
    unsorted_list = convert_list(mixed_list)
    if len(unsorted_list) < 2:
        sorted_list = unsorted_list
        return sorted_list
    else:
        pivot_point = unsorted_list[0]
        larger_list = [num for num in unsorted_list[1:] if num > pivot_point]
        smaller_list = [num for num in unsorted_list[1:] if num <= pivot_point]
        return quick_sort(smaller_list)+[pivot_point]+quick_sort(larger_list)

def selection_sort(mixed_list):
    unsorted_list = convert_list(mixed_list)
    list_length = len(unsorted_list)
    for val in range(list_length):
        leastVal = val
        for compareVal in range(val+1, list_length):
            if unsorted_list[compareVal] < unsorted_list[leastVal]:
                leastVal = compareVal
        tmp = unsorted_list[leastVal]
        unsorted_list[leastVal] = unsorted_list[val]
        unsorted_list[val] = tmp
    sorted_list = unsorted_list
    return sorted_list

if __name__ == '__main__':
    if len(sys.argv) > 2:
        mixed_list = []
        # Slice off sys.argv[0] (program filename, sorting_algorithms.py)
        for element in sys.argv[2:]:
            mixed_list.append(element)
    else:
        sys.exit(1)

    if sys.argv[1] == 'bubble':
        print(bubble_sort(mixed_list))
    elif sys.argv[1] == 'quick':
        print(quick_sort(mixed_list))
    elif sys.argv[1] == 'selection':
        print(selection_sort(mixed_list))
    else:
        print("Not Valid Sorting Algorithm")
        sys.exit(1)


