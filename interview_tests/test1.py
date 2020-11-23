# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/18 11:30 上午
# file: test1.py
# IDE: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def reverse_list(head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return head
        r = head
        l = m = None
        while r.next:
            l = m
            m = r
            r = r.next
            m.next = l
        r.next = m
        return r

    @staticmethod
    def reverse_list1(head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre

    #######
    @staticmethod
    def reverse_list2(head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        head_node = Solution.reverse_list2(head.next)
        head.next.next = head
        head.next = None
        return head_node

    @staticmethod
    def reverse_list3(head):
        if head is None or head.next is None:
            return head
        pre = None
        cur = head
        while cur:
            tmp = cur
            cur = tmp.next
            tmp.next = pre
            pre = tmp
        return pre


if __name__ == '__main__':
    # 单链表反转
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    tmp = l1
    while tmp:
        print(tmp.val)
        tmp = tmp.next
    l4 = Solution.reverse_list3(l1)
    tmp = l4
    while tmp:
        print(tmp.val)
        tmp = tmp.next

    # 双链表反转
