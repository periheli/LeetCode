# pyright: reportRedeclaration=false
from typing import Optional


class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None


class Solution:
    def reverse(self, head: ListNode | None) -> ListNode | None:
        prev, curr = None, head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverse_sub_list(self, head: ListNode, p: int, q: int) -> ListNode:
        if p == q:
            return head

        idx, prev, curr = 1, None, head
        while (curr is not None) and (idx < p):
            prev = curr
            curr = curr.next
            idx += 1

        last_node_of_first_part = prev
        last_node_of_sub_list = curr
        while (curr is not None) and (idx <= q):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            idx += 1

        if last_node_of_first_part is not None:
            last_node_of_first_part.next = prev
        else:
            head = prev
        last_node_of_sub_list.next = curr
        return head

    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        group_start = head
        while True:
            prev, curr = prev_group_end, group_start
            for _ in range(k):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                if curr is None:
                    prev_group_end.next = prev
                    group_start.next = None
                    return dummy.next
            prev_group_end.next = prev
            prev_group_end = group_start
            group_start = curr

    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head

        prev, curr = None, head
        while True:
            last_node_of_prev_part = prev
            last_node_of_sub_list = curr
            idx = 0
            while (curr is not None) and (idx < k):
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                idx += 1

            if last_node_of_prev_part is not None:
                last_node_of_prev_part.next = prev
            else:
                head = prev

            if curr is None:
                last_node_of_sub_list.next = None
                return head

            prev = last_node_of_sub_list

    def reverse_alt_k_group(self, head: ListNode, k: int) -> ListNode:
        if k <= 1:
            return head

        prev, curr = None, head
        is_alt = True
        while True:
            if is_alt:
                last_node_of_prev_part = prev
                last_node_of_sub_list = curr
                idx = 0
                while (curr is not None) and (idx < k):
                    next = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next
                    idx += 1

                if last_node_of_prev_part is not None:
                    last_node_of_prev_part.next = prev
                else:
                    head = prev

                if curr is None:
                    last_node_of_sub_list.next = None
                    return head

                prev = last_node_of_sub_list
                is_alt = False
            else:
                prev.next = curr
                for _ in range(k):
                    prev = curr
                    curr = curr.next
                    if curr is None:
                        return head
                is_alt = True

    def rotate(self, head: ListNode, k: int) -> ListNode:
        if (head is None) or (head.next is None) or (k <= 0):
            return head

        curr, length = head, 1
        while curr.next is not None:
            curr = curr.next
            length += 1
        tail = curr

        k %= length
        if k == 0:
            return head
        k = length - k
        curr = head
        for _ in range(k - 1):
            curr = curr.next
        tail.next = head
        head = curr.next
        curr.next = None
        return head
