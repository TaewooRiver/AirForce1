data_1 = [7,5,9,0,3,1,6,2,4,8]
data_2 = [7,5,9,0,3,1,6,2,4,8]
data_3 = [7,5,9,0,3,1,6,2,4,8]
data_4 = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

#  파이썬은 변수끼리 스왑하는 게 매우 쉽다(그것마저 귀찮아서 함수로 만들었지만)
def swapListElement(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list

# 선택 정렬
# 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞의 것과 바꾼다.
def selectionSort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                swapListElement(list, min_index, j)
    return list

# 삽입 정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입한다.
def insertionSort(list):
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                swapListElement(list, j, j - 1)
            else:
                break
    return list

# 퀵 정렬 O(NlogN)
# 기준 데이터를 설정하고 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
def quickSort(list, start, end):
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
        if left > right:
            swapListElement(list, right, pivot)
        else:
            swapListElement(list, left, right)
    quickSort(list, start, right - 1)
    quickSort(list, right + 1, end)
    return list

# 계수 정렬
# 각 원소가 존재하는 갯수를 저장할 리스트를 만들고, 
# 그 리스트를 오름차순으로 반환하면 정렬된 결과가 나온다.
def countSort(list):
    count = [0] * (max(list) + 1)
    res = []
    for i in range(len(list)):
        count[list[i]] += 1
    for i in range(len(count)):
        for j in range(count[i]):
            res.append(i)
    return res

print(selectionSort(data_1))
print(insertionSort(data_2))
print(quickSort(data_3, 0, len(data_3) - 1))
print(countSort(data_4))