n = int(input())
q = []
for i in range(n):
    
    q.append(input().split())

q.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in q:
    print(i[0])


# def swapListElement(list, a, b):
#     list[a], list[b] = list[b], list[a]
#     return list

# def quickSort(list, start, end):
#     if start >= end:
#         return list
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         while left <= end and list[left] <= list[pivot]:
#             left += 1
#         while right > start and list[right] >= list[pivot]:
#             right -= 1
#         if left > right:
#             swapListElement(list, right, pivot)
#         else:
#             swapListElement(list, right, left)
#     quickSort(list, start, right - 1)
#     quickSort(list, right + 1, end)
#     return list
#