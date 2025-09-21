# pyright: reportRedeclaration=false
import bisect
import math
import operator
import random
import re
from collections import Counter, deque
from heapq import (
    heapify,
    heappop,
    heappush,
    heappushpop,
    heapreplace,
    merge,
    nlargest,
)
from itertools import accumulate
from os import dup
from turtle import left
from typing import Dict, List, Optional, Set, Tuple

from sortedcontainers import SortedList


class Solution:
    def sort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):  # len(nums) - 1 is also ok
            while i != (nums[i] - 1):
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        return nums

    def find_missing_number(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while (i != nums[i]) and (nums[i] != n):
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
        for i, num in enumerate(nums):
            if num == n:
                return i
        return n

    def find_numbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            # while (i != (nums[i] - 1)) and (nums[i] != nums[nums[i] - 1]):
            while nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        missing_numbers = [i + 1 for i in range(n) if i != (nums[i] - 1)]
        return missing_numbers

    def find_duplicate(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            while i != (nums[i] - 1):
                j = nums[i] - 1
                if nums[i] == nums[j]:
                    return nums[i]
                nums[i], nums[j] = nums[j], nums[i]
        return -1

    def find_duplicate_no_swap(self, nums: list[int]) -> int:
        fast, slow = nums[0], nums[nums[0]]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        # find cycle length
        cycle_len = 0
        current = slow
        while True:
            current = nums[current]
            cycle_len += 1
            if current == slow:
                break
        ptr1 = ptr2 = 0
        for _ in range(cycle_len):
            ptr2 = nums[ptr2]
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1

    def find_all_duplicates(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        duplicates = [num for i, num in enumerate(nums) if i != (num - 1)]
        return duplicates
