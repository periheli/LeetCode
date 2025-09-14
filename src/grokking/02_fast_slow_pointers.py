# pyright: reportRedeclaration=false
import bisect
import math
import operator
import random
from collections import Counter, deque
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, nlargest
from itertools import accumulate
from turtle import left
from typing import Dict, List, Optional, Set, Tuple

from sortedcontainers import SortedList


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None


class Solution:
    # 141. Linked List Cycle
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = low = head
        while fast is not None and fast.next is not None:
            low = low.next
            fast = fast.next.next
            if low is fast:
                return True
        return False

    def findMiddle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while True:
            if fast.next is None:
                return slow
            if fast.next.next is None:
                return slow.next
            slow = slow.next
            fast = fast.next.next

    def findMiddle2(self, head: ListNode) -> ListNode:
        slow = fast = head
        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def cycle_length(self, slow: ListNode) -> int:
        current = slow
        length = 0
        while True:
            current = current.next
            length += 1
            if current is slow:
                break
        return length

    def find_start(self, head: ListNode, cycle_length: int) -> ListNode:
        ptr1 = ptr2 = head
        for _ in range(cycle_length):
            ptr2 = ptr2.next
        while ptr1 is not ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1

    def find_cycle_start(self, head: ListNode) -> ListNode | None:
        slow = fast = head
        cycle_length = 0
        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                cycle_length = self.cycle_length(slow)
                break
        if cycle_length == 0:
            return None
        return self.find_start(head, cycle_length)

    def square_digits(self, num: int) -> int:
        result = 0
        while num > 0:
            digit = num % 10
            result += digit * digit
            num //= 10
        return result

    def is_happy(self, num: int) -> bool:
        slow = fast = num
        while fast != 1:
            slow = self.square_digits(slow)
            fast = self.square_digits(self.square_digits(fast))
            if slow == fast:
                return slow == 1
        return True

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def check_palindrome(self, left: ListNode, right: ListNode) -> bool:
        # assume left is equal or longer than right
        while right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def is_palindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        slow = fast = head
        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        tail = self.reverse(slow)
        is_pal = self.check_palindrome(head, tail)
        self.reverse(tail)
        return is_pal

    def insert_second_half(self, left: ListNode, right: ListNode) -> ListNode:
        # assume left is equal or longer than right
        left_curr, right_curr = left, right
        while right_curr is not None:
            right_next = right_curr.next
            right_curr.next = left_curr.next
            left_curr.next = right_curr
            left_curr = right_curr.next
            right_curr = right_next
        return left

    def reorder(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        slow = fast = head
        while (fast is not None) and (fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        if slow.next is None:
            return head

        tail = self.reverse(slow.next)
        return self.insert_second_half(head, tail)

    def loop_exists(self, arr: List[int]) -> bool:
        n = len(arr)

        def move(index: int, direction: int) -> int:
            next_idx = (index + arr[index]) % n
            if next_idx == index or (arr[index] * direction < 0):
                return -1
            return next_idx

        visited = [False] * n
        for i in range(n):
            if visited[i]:
                continue
            direction = 1 if arr[i] > 0 else -1
            slow = fast = i
            visited[i] = True
            while True:
                slow = move(slow, direction)
                fast = move(fast, direction)
                if fast == -1:
                    break
                visited[fast] = True
                fast = move(fast, direction)
                if fast == -1:
                    break
                visited[fast] = True
                if slow == fast:
                    return True
        return False
