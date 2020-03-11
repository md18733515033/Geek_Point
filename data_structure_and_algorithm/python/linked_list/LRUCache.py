# Definition for double singly-linked list.
class DbListNode(object):
    """构建一个双向链表"""
    def __init__(self, x, y):
        self.key = x
        self.val = y
        self.next = None
        self.prev = None


class LRUCache(object):
    '''
    leet code: 146
    运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
    它应该支持以下操作： 获取数据 get 和 写入数据 put 。
    获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
    写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
        缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间
    实现方式: 哈希表+双向链表
    哈希表: 查询 O(1)
    双向链表: 有序, 增删操作 O(1)
    Author: Ben
    '''

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hkeys = {}
        # self.top和self.tail作为哨兵节点, 避免越界
        self.top = DbListNode(None, -1)
        self.tail = DbListNode(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self, key: int) -> int:
        """获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。"""
        if key in self.hkeys.keys():
            # 获取节点的数据
            cur = self.hkeys[key]
            # 从双向链表中将cur取出来
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            # 获取最近的最新节点
            top_node = self.top.next
            # 将cur节点放到节点的第一位
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
            return self.hkeys[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        """
        写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
        当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间
        """
        if key in self.hkeys.keys():
            # 获取节点的数据
            cur = self.hkeys[key]
            # 从双向链表中将cur取出来
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            # 获取最近的最新节点
            top_node = self.top.next
            # 将cur节点放到节点的第一位
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
        else:
            cur = DbListNode(key, value)
            # 先判断现在的长度是否和容量相等,如果相等就先去除尾端节点
            if len(self.hkeys.keys()) == self.cap:
                self.hkeys.pop(self.tail.prev.key)
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
            self.hkeys[key] = cur
            # 获取最新用过的链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    cache.get(1)  # 返回  1
    print(cache)
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    print(cache)
    cache.get(2)  # 返回 -1 (未找到)
    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    print(cache)
    cache.get(1)  # 返回 -1 (未找到)
    cache.get(3)  # 返回  3
    print(cache)
    cache.get(4)  # 返回  4
    print(cache)