'''
Given a sorted array that may have duplicate values, use binary search to find the first and last indexes of a given value.
For example, if you have the array [0, 1, 2, 2, 3, 3, 3, 4, 5, 6] and the given value is 3, the answer will be
[4, 6] (because the value 3 occurs first at index 4 and last at index 6 in the array).
The expected complexity of the problem is  𝑂(𝑙𝑜𝑔(𝑛)) .
'''


def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    # TODO: Write your first_and_last function here
    # Note that you may want to write helper functions to find the start
    # index and the end index

    index = binary_search_recursive_soln(arr,number,0,len(arr)-1)

    count = 0
    indexleft = indexright = index
    while indexright > 0:
        if arr[indexleft-1] == number:
            count += 1
            indexleft = indexleft-1
        else:
            break
    startindex = index - count

    count = 0
    while indexright < len(arr)-1:
        if arr[indexright + 1] == number:
            count += 1
            indexright = indexright + 1
        else:
            break
    endindex = index + count
    mylist = []
    mylist.append(startindex)
    mylist.append(endindex)

    return mylist

def binary_search_recursive_soln(array, target, start_index, end_index):

    if start_index > end_index:
        return -1

    mid = (start_index + end_index) // 2
    midelem = array[mid]

    if midelem == target:
        return mid
    elif target < midelem:
        return binary_search_recursive_soln(array, target, start_index, mid - 1)
    else:
        return binary_search_recursive_soln(array, target, mid+1, end_index)

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)