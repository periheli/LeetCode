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


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class NAryNode:
    def __init__(self, val: int = 0, children: List["NAryNode"] | None = None):
        self.val = val
        self.children = children or []


class Solution:
    def find_level_averages(self, root: TreeNode) -> List[float]:
        level_avgs: List[float] = []
        queue = deque([root])
        while queue:
            n = len(queue)
            level_sum = 0
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_sum += node.val
            level_avgs.append(level_sum / n)
        return level_avgs

    def find_depth(self, root: TreeNode) -> int:
        min_depth = 0
        queue = deque([root])
        while queue:
            n = len(queue)
            min_depth += 1
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.left is None and node.right is None:
                    return min_depth
        return min_depth

    def find_successor(self, root: TreeNode, key: int) -> TreeNode | None:
        queue = deque([root])
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.val == key:
                    return queue[0] if queue else None

    def connect(self, root: TreeNode) -> TreeNode:
        queue = deque([root])
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == (n - 1):
                    node.next = None
                else:
                    node.next = queue[0]
        return root

    def connect_all(self, root: TreeNode) -> TreeNode:
        queue = deque()
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        prev_node = root
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                prev_node.next = node
                prev_node = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

    def right_view(self, root: TreeNode) -> List[int]:
        right_view: List[int] = []
        queue = deque([root])
        while queue:
            n = len(queue)
            right_view.append(queue[-1].val)
            for _ in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return right_view
