from typing import List


def a(n):
    """一共有n个台阶,青蛙一次能跳一个台阶或者一次跳两个台阶,问青蛙到达顶部有多少种方法"""
    if n == 1:
        return 1
    if n == 2:
        return 2
    return a(n-1) + a(n-2)


def merge_sort(a: List[int]):
    """
    归并排序:先处理子问题,然后再合并
    递归思想,先切割为最小再一段一段排起来,顺序是从下往上,而快排是从上往下
    归并排序的处理过程是由下到上的,先处理子问题,然后再合并。
    而快排正好相反,它的处理过程是由上到下的,先分区,然后再处理子问题
    归并排序是稳定的、时间复杂度为 O(nlogn) 的排序算法,但是它是非原地排序算法
    """
    _merge_sort_between(a, 0, len(a) - 1)


def _merge_sort_between(a: List[int], low: int, high: int):
    # The indices are inclusive for both low and high.
    if low < high:
        mid = low + (high - low) // 2
        _merge_sort_between(a, low, mid)
        _merge_sort_between(a, mid + 1, high)
        _merge(a, low, mid, high)


def _merge(a: List[int], low: int, mid: int, high: int):
    # a[low:mid], a[mid+1, high] are sorted.
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if a[i] < a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start: end + 1])
    a[low: high + 1] = tmp


if __name__ == "__main__":
    a1 = [5, -1, 9, 3, 7, 8, 3, -2, 9, 6]
    merge_sort(a1)
    print(a1)