# pyright: reportRedeclaration=false
import math
from collections import defaultdict
from typing import Dict, List, Optional


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
    def min_root_to_leaf_sum(self, root: TreeNode) -> int:
        if root is None:
            return math.inf

        min_left = self.min_root_to_leaf_sum(root.left)
        min_right = self.min_root_to_leaf_sum(root.right)
        return root.val + min(min_left, min_right)

    def has_path(self, root: TreeNode, sum: int) -> bool:
        if root.left is None and root.right is None:
            return root.val == sum

        if root.left:
            if self.has_path(root.left, sum - root.val):
                return True
        if root.right:
            if self.has_path(root.right, sum - root.val):
                return True
        return False

    def find_paths(self, root: TreeNode, required_sum: int) -> List[List[int]]:
        if root.left is None and root.right is None:
            return [[root.val]] if root.val == required_sum else []

        all_paths: List[List[int]] = []
        if root.left:
            left_paths = self.find_paths(root.left, required_sum - root.val)
            all_paths.extend(left_paths)
        if root.right:
            right_paths = self.find_paths(root.right, required_sum - root.val)
            all_paths.extend(right_paths)
        return [[root.val] + path for path in all_paths]

    def sum_all_paths(self, root: TreeNode) -> int:
        def helper(node: TreeNode, current_value: int):
            if node.left is None and node.right is None:
                return current_value
            total_value = 0
            if node.left:
                left_sum = helper(node.left, current_value * 10 + node.left.val)
                total_value += left_sum
            if node.right:
                right_sum = helper(
                    node.right, current_value * 10 + node.right.val
                )
                total_value += right_sum
            return total_value

        return helper(root, root.val)

    def is_present(self, root: TreeNode, sequence: List[int]) -> bool:
        def helper(node: TreeNode, sequence: List[int]):
            if not sequence:
                return False
            if node.val != sequence[0]:
                return False
            if node.left is None and node.right is None:
                return len(sequence) == 1
            if node.left:
                if helper(node.left, sequence[1:]):
                    return True
            if node.right:
                if helper(node.right, sequence[1:]):
                    return True
            return False

        return helper(root, sequence)

    def count_paths(self, root: TreeNode, S: int) -> int:
        def count_full_paths(node: TreeNode, value: int) -> int:
            if node.left is None and node.right is None:
                return 1 if value == node.val else 0
            total = 0
            if node.left:
                total += count_full_paths(node.left, value - node.val)
            if node.right:
                total += count_full_paths(node.right, value - node.val)
            return total

        def count_partial_paths(node: TreeNode, value: int) -> int:
            if node.left is None and node.right is None:
                return 1 if value == node.val else 0
            total = 0
            if node.left:
                total += count_full_paths(node.left, value - node.val)
                total += count_partial_paths(node.left, value)
            if node.right:
                total += count_full_paths(node.right, value - node.val)
                total += count_partial_paths(node.right, value)
            return total

        return count_partial_paths(root, S)

    def count_paths(self, root: TreeNode, S: int) -> int:
        prefix_sum_counter: Dict[int, int] = defaultdict(lambda: 0)
        prefix_sum_counter[0] = 1

        def helper(node: TreeNode, current_sum: int):
            current_sum += node.val
            prefix_sum_counter[current_sum] += 1
            counter = prefix_sum_counter[current_sum - S]
            if node.left:
                counter += helper(node.left, current_sum)
            if node.right:
                counter += helper(node.right, current_sum)
            prefix_sum_counter[current_sum] -= 1
            return counter

        return helper(root, 0)

    def find_diameter(self, root: TreeNode) -> int:
        def find_height(node: TreeNode | None) -> int:
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            return 1 + max(find_height(node.left), find_height(node.right))

        def helper(node: TreeNode) -> int:
            if node.left is None or node.right is None:
                return 0
            diameter = find_height(node.left) + find_height(node.right) + 1
            diameter = max(diameter, helper(node.left), helper(node.right))
            return diameter

        return helper(root)

    def find_path_with_max_sum(self, root: TreeNode) -> int:
        max_sum: int = -math.inf

        def helper(node: TreeNode | None) -> int:
            nonlocal max_sum
            if node is None:
                return 0
            max_left = helper(node.left)
            max_right = helper(node.right)
            current_max = node.val + max(max_left, 0) + max(max_right, 0)
            max_sum = max(max_sum, current_max)
            return node.val + max(max_left, max_right, 0)

        helper(root)
        return max_sum
