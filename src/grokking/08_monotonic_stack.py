# pyright: reportRedeclaration=false
from collections import deque
from typing import Dict, List, Optional, Tuple


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None


class Solution:
    def remove_nodes(self, head: ListNode) -> ListNode:
        decreasing_stack = deque()
        curr = head
        while curr is not None:
            while decreasing_stack and (decreasing_stack[-1].val < curr.val):
                node_to_remove = decreasing_stack.pop()
                if decreasing_stack:
                    decreasing_stack[-1].next = curr
                else:
                    head = curr
                node_to_remove.next = None
                del node_to_remove
            decreasing_stack.append(curr)
            curr = curr.next
        return head

    def remove_duplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and (stack[-1] == char):
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)

    def next_greater_element(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:
        m = len(nums2)
        decreasing_stack: List[int] = []
        nge_list = [-1] * m
        for i in range(m - 1, -1, -1):
            num = nums2[i]
            while decreasing_stack and (decreasing_stack[-1] <= num):
                decreasing_stack.pop()
            if decreasing_stack:
                nge_list[i] = decreasing_stack[-1]
            decreasing_stack.append(num)

        pos_mapping = {num: nge for num, nge in zip(nums2, nge_list)}
        return [pos_mapping[num] for num in nums1]

    def next_greater_element(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:
        decreasing_stack: List[int] = []
        nge_mapping: Dict[int, int] = {}
        for num in nums2:
            while decreasing_stack and (decreasing_stack[-1] < num):
                nge_mapping[decreasing_stack.pop()] = num
            decreasing_stack.append(num)
        return [nge_mapping.get(num, -1) for num in nums1]

    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack: List[Tuple[int, int]] = []
        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            while stack and (stack[-1][0] <= temp):
                stack.pop()
            if stack:
                warmer_idx = stack[-1][1]
                result[i] = warmer_idx - i
            stack.append((temp, i))
        return result

    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack: List[int] = []
        for i, temp in enumerate(temperatures):
            while stack and (temperatures[stack[-1]] < temp):
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result

    def remove_duplicates_2(self, s: str, k: int) -> str:
        stack: List[Tuple[str, int]] = []
        for char in s:
            if stack and (stack[-1][0] == char):
                _, count = stack.pop()
                if count < (k - 1):
                    stack.append((char, count + 1))
            else:
                stack.append((char, 1))
        return "".join([char * count for char, count in stack])

    def sum_sub_arr_mins(self, arr: List[int]) -> int:
        stack: List[Tuple[int, int]] = []
        stack_sum = 0
        result = 0
        for num in arr:
            total_count = 1
            while stack and (stack[-1][0] >= num):
                value, count = stack.pop()
                stack_sum -= value * count
                total_count += count
            stack.append((num, total_count))
            stack_sum += num * total_count
            result += stack_sum
        return result

    def remove_k_digits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        stack: List[str] = []
        i = 0
        for i in range(len(num)):
            char = num[i]
            while stack and (stack[-1] > char):
                stack.pop()
                k -= 1
                if k == 0:
                    return ("".join(stack) + num[i:]).lstrip("0") or "0"
            stack.append(char)
        return "".join(stack[:-k]).lstrip("0") or "0"
