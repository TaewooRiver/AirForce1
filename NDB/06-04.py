data = [7,5,9,0,3,1,6,2,4,8]

def swapListElement(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list

def quickSort2(list, start, end):
    if start >= end:
        return list
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and list[left] <= list[pivot]:
            left += 1
        while right > start and list[right] >= list[pivot]:
            right -= 1
        if right < left:
            swapListElement(list, right, pivot)
        else:
            swapListElement(list, right, left)
    quickSort2(list, start, right - 1)
    quickSort2(list, right + 1, end)
    return list

print(quickSort2(data, 0, len(data) - 1))
