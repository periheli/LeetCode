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
from typing import Dict, List, Optional, Set, Tuple

from sortedcontainers import SortedList


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None


class Solution:
    def first_uniq_char(self, s: str) -> int:
        counter = Counter(s)
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        return -1

    def largest_uniq_num(self, nums: List[int]) -> int:
        counter = Counter(nums)
        idx = -1
        for i, num in enumerate(nums):
            if counter[num] == 1:
                if (idx == -1) or (num > nums[idx]):
                    idx = i
        return idx

    def count_balloon(self, text: str) -> int:
        counter = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for char in text:
            if char in counter:
                counter[char] += 1
        result = min(
            min(counter.values()), min(counter["l"], counter["o"]) // 2
        )
        return result

    def longest_palindrome(self, s: str) -> int:
        counter = Counter(s)
        has_odd = any(count % 2 == 1 for count in counter.values())
        return has_odd + sum(
            count if count % 2 == 0 else count - 1 for count in counter.values()
        )

    def can_construct(self, note: str, magazine: str) -> bool:
        note_counter = Counter(note)
        for char in magazine:
            if char in note_counter:
                note_counter[char] -= 1
                if note_counter[char] == 0:
                    note_counter.pop(char)
                    if len(note_counter) == 0:
                        return True
        return False
