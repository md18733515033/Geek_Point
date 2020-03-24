import random
from typing import List


def quick_sort(a: List[int]):
    """快排是一种原地、不稳定的排序算法"""
    _quick_sort_between(a, 0, len(a)-1)


def _quick_sort_between(a: List[int], low: int, high: int):
    if low < high:
        # get a random position as the pivot
        # 因为每次都是取第一个数,这样生成随机数和第一个数进行交换就达到了随机选取列表中一个数作为分区点的目的
        k = random.randint(low, high)
        a[low], a[k] = a[k], a[low]

        m = _partition(a, low, high)  # a[m] is in final position
        _quick_sort_between(a, low, m - 1)
        _quick_sort_between(a, m + 1, high)


def _partition(a: List[int], low: int, high: int):
    pivot, j = a[low], low
    for i in range(low + 1, high + 1):
        if a[i] <= pivot:
            j += 1
            print(a[i], a[j])
            a[j], a[i] = a[i], a[j]  # swap
            print(a)
    a[low], a[j] = a[j], a[low]
    return j


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a4)
    print(a4)

