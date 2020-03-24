def select_sort(arr: list):
    """
    原地排序,不稳定排序,时间复杂度: 最好O(n^2) 最差O(n^2) 平均O(n^2)
    选择排序算法的实现思路有点类似插入排序,也分已排序区间和未排序区间。但是选择排序每次会从未排序区间中找到最小的元素,将其放到已排序区间的末尾。
    :param arr: 要排序的列表
    :return:
    """
    for x in range(len(arr) - 1):
        min_point = x
        for y in range(x + 1, len(arr)):
            if arr[y] < arr[min_point]:
                min_point = y

        if arr[x] != arr[min_point]:
            print(arr[x], min_point)
            arr[x], arr[min_point] = arr[min_point], arr[x]

    return arr


print(select_sort([111, 33, 45, 22, 8, 3, 6, 78]))
