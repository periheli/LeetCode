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


class Solution:
    def is_valid_parentheses(self, s: str) -> bool:
        stack = deque()
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                if len(stack) == 0:
                    return False
                top_element = stack.pop()
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0

    def reverse_string(self, s: str) -> str:
        from collections import deque

        stack = deque()
        for char in s:
            stack.append(char)
        reversed = ""
        while stack:
            reversed += stack.pop()
        return reversed

    def decimal_to_binary(self, num: int) -> str:
        from collections import deque

        if num == 0:
            return "0"

        stack = deque()
        while num > 0:
            stack.append(num % 2)
            num //= 2
        binary = ""
        while stack:
            binary += str(stack.pop())
        return binary

    def next_larger_element(self, arr: List[int]) -> List[int]:
        from collections import deque

        nge_list = [-1] * len(arr)

        increasing_stack = deque()
        for i in range(len(arr) - 1, -1, -1):
            num = arr[i]
            while increasing_stack and (increasing_stack[-1] <= num):
                increasing_stack.pop()
            if increasing_stack:
                nge_list[i] = increasing_stack[-1]
            increasing_stack.append(num)
        return nge_list

    def sort_stack(self, stack: List[int]) -> List[int]:
        from collections import deque

        temp_stack = deque()
        while stack:
            top = stack.pop()
            while temp_stack and (temp_stack[-1] > top):
                stack.append(temp_stack.pop())
            temp_stack.append(top)
        return list(temp_stack)

    def simplify_path(self, path: str) -> str:
        from collections import deque

        dirs = path.split("/")
        dirs = [d for d in dirs if d and (d not in [".", ""])]
        stack = deque()
        for d in dirs:
            if d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        return "/" + "/".join(stack)
