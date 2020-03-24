chaos = [2, 6, 3, 100, 7, 9, 5]


def bubble_sort(chaos_list: list):
    """
    原地排序,稳定排序,时间复杂度: 最好O(n) 最差O(n^2) 平均O(n^2)
    :param chaos_list:
    :return:
    """
    for x in range(len(chaos_list)):
        flag = False
        for y in range(1, len(chaos_list)):
            if chaos_list[y] < chaos_list[y - 1]:
                chaos_list[y], chaos_list[y - 1] = chaos_list[y - 1], chaos_list[y]
                flag = True
        # 每次循环完看该次是否有改变,如果没有改变说明现在已经有序了,无需再进行下面的排序
        if flag:
            continue
        else:
            return chaos_list
