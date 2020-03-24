def a(n):
    """一共有n个台阶,青蛙一次能跳一个台阶或者一次跳两个台阶,问青蛙到达顶部有多少种方法"""
    if n == 1:
        return 1
    if n == 2:
        return 2
    return a(n-1) + a(n-2)

