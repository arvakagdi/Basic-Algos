def binary_search_recursive(array, target):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


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

#finds the first occurence of the number
def find_first(source,target):
    index = binary_search_recursive(source,target)   #get index
    if not index:
        return None
    while source[index] == target:          #untill given index is target
        if index == 0:
            return 0
        if source[index-1] == target:
            index -= 1
        else:
            return index

multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(multiple,7)) # Should return 3
print(find_first(multiple,9)) # Should return None


def contains(source,target):
    index = binary_search_recursive(source,target)
    if not index:
        return False
    if index == -1:
        return False
    else:
        return True

letters = [1,2,3,4,5]
print(contains(letters,5)) ## True
print(contains(letters,7)) ## False

def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = -1
index = -1
test_case = [array, target, index]
test_function(test_case)

array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
index = -1
test_case = [array, target, index]
test_function(test_case)