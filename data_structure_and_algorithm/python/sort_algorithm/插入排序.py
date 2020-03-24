from typing import List


def insert_sort(arr: List[int]):
    """
    原地排序,稳定排序,时间复杂度: 最好O(n) 最差O(n^2) 平均O(n^2)
    直接插入排序是插入排序的一种，核心思想就是将整个序列看成两部分，有序和无序，从第二个元素开始遍历，每次取出一个跟其左边那个元素比较，
    比左边邻居大说明不用动，比其小，就需要将该元素取出，然后遍历左半边有序序列部分，通过比较大小找出该插入的位置插之，观察代码可知，
    该算法的最好时间复杂度为O(n^2),空间复杂度为O(1)，且是稳定性算法。
    :param arr: 需要排序的列表
    :return:
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr


print(insert_sort([4, 100, 6, 32, 8, 1, 3, 2, 0]))

