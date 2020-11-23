# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/18 2:09 下午
# file: test2.py
# IDE: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    @staticmethod
    def revrse_list(head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.left is None and head.right is None:
            return head
        pre = None
        while head:
            next = head.right
            head.right = pre
            head.left = next
            pre = head
            head = next
        return pre



