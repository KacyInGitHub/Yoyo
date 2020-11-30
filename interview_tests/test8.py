# -*- coding:utf-8 -*-
# author: lining3
# date: 2020/11/24 11:04 上午
# file: test8.py
# IDE: PyCharm


class Sort:

    # 交换排序
    @staticmethod
    def bubble_sort(l):
        for i in range(len(l)-1):
            for j in range(len(l)-1-i):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]
    # 交换排序
    @staticmethod
    def quick_sort(data, start, end):
        i = start
        j = end
        if i >= j:
            return
        flag = data[start]
        while i < j:
            while i < j and data[j] > flag:
                j -= 1
            data[i] = data[j]
            while i < j and data[i] < flag:
                i += 1
            data[j] = data[i]
        data[i] = flag
        Sort.quick_sort(data, start, i-1)
        Sort.quick_sort(data, i+1, end)

    # 简单选择排序
    @staticmethod
    def select(data):
        for i in range(len(data)):
            min_index = i
            for j in range(i+1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]

    # 选择排序-堆排序
    @staticmethod
    def heapify(data, n, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < n and data[left] > data[largest]:
            largest = left
        if right < n and data[right] > data[largest]:
            largest = right
        if largest != i:
            data[largest], data[i] = data[i], data[largest]
            Sort.heapify(data, n, largest)

    @staticmethod
    def heap_sort(data):
        n = len(data)

        for i in range(n, -1, -1):
            Sort.heapify(data, n, i)

        for i in range(n-1, 0, -1):
            data[0], data[i] = data[i], data[0]
            Sort.heapify(data, i, 0)


if __name__ == '__main__':
    # l = [6,5,4,3,2,1]
    # Sort.bubble_sort(l)
    # print(l)
    #
    # l = [6,5,3,2,1]
    # Sort.quick_sort(l, 0, len(l) - 1)
    # print(l)
    #
    # l = [6,5,4,3,1,2]
    # Sort.select(l)
    # print(l)

    l = [6, 5, 4, 3, 1, 2]
    Sort.heap_sort(l)
    print(l)
