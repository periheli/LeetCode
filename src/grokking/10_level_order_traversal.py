# pyright: reportRedeclaration=false
from collections import deque
from typing import List, Optional


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
    def traverse(self, root: TreeNode):
        result: deque[deque[TreeNode]] = deque()
        node_queue = deque([root])

        while node_queue:
            curr_level_node: deque[TreeNode] = deque()
            n = len(node_queue)
            for _ in range(n):
                node = node_queue.pop()
                curr_level_node.append(node)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            result.appendleft(curr_level_node)
        return result

    def largest_values(self, root: TreeNode) -> List[int]:
        result: deque[int] = deque()
        node_queue = deque([root])
        while node_queue:
            n = len(node_queue)
            max_value = node_queue[0].val
            for _ in range(n):
                node = node_queue.popleft()
                max_value = max(max_value, node.val)
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            result.append(max_value)
        return list(result)

    def width_of_bin_tree(self, root: TreeNode) -> int:
        max_width = 1
        node_queue = deque([(root, 0)])
        while node_queue:
            n = len(node_queue)
            start = node_queue[0][1]
            end = 0
            for _ in range(n):
                node, idx = node_queue.popleft()
                end = idx
                if node.left:
                    node_queue.append((node.left, 2 * idx))
                if node.right:
                    node_queue.append((node.right, 2 * idx + 1))
            max_width = max(max_width, end - start + 1)
        return max_width

    def max_level_sum(self, root: TreeNode) -> int:
        max_sum = root.val
        max_level = 1
        node_queue = deque([root])
        level = 0
        while node_queue:
            n = len(node_queue)
            level += 1
            level_sum = 0
            for _ in range(n):
                node = node_queue.popleft()
                level_sum += node.val
                if node.left:
                    node_queue.append(node.left)
                if node.right:
                    node_queue.append(node.right)
            if level_sum > max_sum:
                max_level = level
                max_sum = level_sum
        return max_level

    def zigzag_traverse(self, root: TreeNode) -> List[List[int]]:
        result: deque[List[int]] = deque()
        queue = deque([root])
        reverse = False
        while queue:
            n = len(queue)
            level_values: deque[int] = deque()
            for _ in range(n):
                node = queue.popleft()
                if reverse:
                    level_values.appendleft(node.val)
                else:
                    level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            reverse = not reverse
            result.append(list(level_values))
        return list(result)

    def is_even_odd_tree(self, root: TreeNode) -> bool:
        is_odd = False
        queue = deque([root])
        while queue:
            n = len(queue)
            mod_two = 0 if is_odd else 1
            curr_val = 10**7 if is_odd else 0
            for _ in range(n):
                node = queue.popleft()
                if (node.val % 2) != mod_two:
                    return False
                if is_odd and (node.val >= curr_val):
                    return False
                if (not is_odd) and (node.val <= curr_val):
                    return False
                curr_val = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            is_odd = not is_odd
        return True

    def level_order(self, root: NAryNode) -> List[List[int]]:
        result: deque[List[int]] = deque()
        queue = deque([root])
        while queue:
            n = len(queue)
            values: deque[int] = deque()
            for _ in range(n):
                node = queue.popleft()
                values.append(node.val)
                for child in node.children:
                    queue.append(child)
            result.append(list(values))
        return list(result)
