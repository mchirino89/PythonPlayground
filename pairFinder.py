def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)

def matchFinder():
    sortedArrayA = [17, 35, 40, 59, 60]
    sortedArrayB = [13, 25, 35, 59, 75]
    foundIndex = 0


    for index, item in enumerate(sortedArrayA):
        # print("{} - {}".format(index, item))
        foundIndex = binary_search_recursive(sortedArrayB, item, foundIndex, len(sortedArrayB))
        if foundIndex != -1:
            foundIndex = binary_search_recursive(sortedArrayB, item, foundIndex, len(sortedArrayB))
        else:
            

    

matchFinder()
