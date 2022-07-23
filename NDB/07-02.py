def binary_search(list, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if list[mid] == target:
        return mid
    elif list[mid] < target:
        return binary_search(list, target, mid + 1, end)
    else:
        return binary_search(list, target, start, mid - 1)
    
array = [1,3,5,7,9,11,13,15,17,19]
length = len(array)
target = 7

print(binary_search(array, target, 0, length - 1) + 1)