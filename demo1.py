#!/usr/bin/env python3
# coding=utf-8
# b = [1, 1, 1, 2]


# def find_uniue(arr):
#     a, b = set(arr)
#     return a if arr.count(arr) == 1 else b
# print(find_uniue())


a = "2 4 7 8 10"
b = "1 1 1 1 2"


def iq_test(numbers):
    num = list(map(lambda x: x % 2, map(int, numbers.split(" "))))
    a, b = set(num)
    return num.index(a) + 1 if num.count(a) == 1 else num.index(b) + 1


print(iq_test(a))
