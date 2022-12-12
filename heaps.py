from heapq import heappush, heapify, heappop

'''
1. Порядковая статистика.
Дан массив целых чисел arr и целое число k. Нужно найти элемент, которые в отсортированном
по возрастанию массиве лежит на k-ой позиции.
'''


def get_kth_element(arr: list, k: int):
    arr = sorted(arr)
    for i in range(len(arr)):
        if i == k:
            return arr[i]


def solution():
    arr = list(map(int, input().split()))
    k = int(input())
    print(get_kth_element(arr, k))


'''
2. Слияние K отсортированных массивов.**  
Даны K отсортированных по возрастанию массивов arrs. Нужно получить массив, который содержит 
все элементы из этих массивов и тоже отсортирован по возрастанию. Сортировку использовать 
запрещено. heapq.merge тоже, но можно почитать код для вдохновения. Если хотите использовать 
кучу, то используйте реализацию в модуле heapq, самописная реализация на питоне будет медленней 
и может не пройти тесты.
'''


def read_multiline_input():
    arrays = []
    while True:
        arr = input()
        if arr != '.':
            arr = list(map(int, arr.split()))
            arrays.append(arr)
        else:
            break
    return arrays


def merge_k_sorted(arrays: list) -> list:
    head = []
    heap = [(h[0], i) for i, h in enumerate(arrays) if h]
    heapify(heap)

    while heap:
        data, index = heappop(heap)
        head.append(data)
        if arrays[index]:
            arrays[index].pop(0)
        node = arrays[index]
        if node:
            heappush(heap, (node[0], index))
    return head


def solution():
    arrays = read_multiline_input()  # эта функция уже написана
    merged = merge_k_sorted(arrays)
    print(' '.join([str(el) for el in merged]))
