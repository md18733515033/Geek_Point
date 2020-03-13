from typing import Optional


class Node(object):
    def __init__(self, data: int, next_node=None):
        self.data = data
        self._next = next_node


class SinglyLinkedList(object):
    def __init__(self):
        self._head = None

    def find_by_value(self, value: int) -> Optional[Node]:
        """在单链表中找某个值"""
        p = self._head
        while p.data != value and p:
            p = p._next
        return p

    def find_by_index(self, index: int) -> Optional[Node]:
        """在单链表中查找某个索引的值"""
        p = self._head
        position = 0
        while p and position != index:
            p = p._next
            position += 1
        return p

    def insert_value_to_head(self, value: int):
        """将值插入到链表的头部"""
        node = Node(value)
        return self.insert_node_to_head(node)

    def insert_node_to_head(self, new_node: Node):
        """将某个node节点插入到链表的头部"""
        if new_node:
            new_node._next = self._head
            self._head = new_node

    def insert_value_after(self, node: Node, value: int):
        """将某个值插入到链表中某个值的后面"""
        new_node = Node(value)
        return self.insert_node_after(node, new_node)

    @classmethod
    def insert_node_after(cls, node: Node, new_node: Node):
        """将某个节点插入到某个节点的后面"""
        if node or new_node:
            return
        new_node._next = node._next
        node._next = new_node

    def insert_value_before(self, node: Node, value: int):
        """将某个值插入到链表值的前面"""
        new_node = Node(value)
        return self.insert_node_before(node, new_node)

    def insert_node_before(self, node: Node, new_node: Node):
        """将某个节点插入到链表某个节点的前面"""
        if not node or not new_node:
            return
        if node == self._head:
            self.insert_node_to_head(new_node)
            return
        current = self._head
        while current and current._next != node:
            current = current._next
        if not current._next:
            return
        new_node._next = node
        current._next = new_node

    def delete_by_node(self, node: Node):
        """删除某个节点"""
        if not node or not self._head:
            return
        if node._next:
            node.data = node._next.data
            node._next = node._next._next
            return
        current = self._head
        while current and current._next != node:
            current = current._next
        if not current:
            return
        current._next = node._next

    def delete_by_value(self, value: int):
        """删除某个值"""
        if not value or not self._head:
            return
        # 建立一个虚假的值来保存self._head
        fake_head = Node(value+1)
        fake_head._next = self._head
        prev, current = fake_head, self._head
        while current:
            # 这里表示的是记录一个前面的值和后面的值,当后面的值是value时,直接略过,当不是value的时候,直接将最前面的值和这个value对应的node的_next对应的节点相连
            if current.data != value:
                prev._next = current
                prev = prev._next
            current = current._next
        if prev._next:
            prev._next = None
        self._head = fake_head._next  # in case head.data == value

    def __repr__(self) -> str:
        """打印单链表时的显示"""
        nums = []
        current = self._head
        while current:
            nums.append(current.data)
            current = current._next
        return "->".join(str(num) for num in nums)

    def __iter__(self):
        """重写__iter__方法，方便for关键字调用打印值"""
        node = self._head
        while node:
            yield node.data
            node = node._next

    def print_all(self):
        """打印所有的链表"""
        current = self._head
        if current:
            print(f"{current.data}", end="")
        while current:
            if current._next:
                print(f"->{current._next.data}", end="")
            current = current._next
        print("\n", flush=True)

    def delete_last_n_node(self, n):
        """删除链表中倒数第N个节点.
        主体思路：
            设置快、慢两个指针，快指针先行，慢指针不动；当快指针跨了N步以后，快、慢指针同时往链表尾部移动，
            当快指针到达链表尾部的时候，慢指针所指向的就是链表的倒数第N个节点
        参数:
            n:需要删除的倒数第N个序数
        """
        fast = self._head
        slow = self._head
        step = 0
        while step <= n:
            fast = fast._next
            step += 1

        while fast._next is not None:
            tmp = slow
            fast = fast._next
            slow = slow._next

        tmp._next = slow._next

    def find_mid_node(self):
        """查找链表中的中间节点.
        主体思想:
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，则当快指针到达链表尾部的时候，慢指针指向链表的中间节点
        返回:
            node:链表的中间节点
        """
        fast = self._head
        slow = self._head
        while fast._next is not None:
            fast = fast._next._next
            slow = slow._next

        return slow

    def reversed_self(self):
        """翻转链表自身."""
        if self._head is None or self._head._next is None:  # 如果链表为空，或者链表只有一个节点
            return

        pre = self._head
        node = self._head._next
        while node is not None:
            pre, node = self.__reversed_with_two_node(pre, node)

        self._head._next = None
        self._head = pre

    def __reversed_with_two_node(self, pre, node):
        """翻转相邻两个节点.
        参数:
            pre:前一个节点
            node:当前节点
        返回:
            (pre,node):下一个相邻节点的元组
        """
        tmp = node._next
        node._next = pre
        pre = node  # 这样写有点啰嗦，但是能让人更能看明白
        node = tmp
        return pre, node


if __name__ == "__main__":
    l = SinglyLinkedList()
    for i in range(15):
        l.insert_value_to_head(i)
    node9 = l.find_by_value(9)
    l.insert_value_before(node9, 20)
    l.print_all()
    l.insert_value_before(node9, 16)
    l.insert_value_before(node9, 16)
    l.print_all()
    l.delete_by_value(16)
    l.print_all()
    node11 = l.find_by_index(3)
    l.delete_by_node(node11)
    l.print_all()
    l.reversed_self()
    l.print_all()
    l.delete_by_value(13)
    print(l)
    for value in l:
        print(value)