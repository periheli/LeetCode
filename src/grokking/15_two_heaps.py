import heapq


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end


class Solution:
    def __init__(self):
        self.left_heap: list[int] = []
        self.right_heap: list[int] = []

    def insertNum(self, num: int):
        if len(self.left_heap) < len(self.right_heap):
            if num <= self.right_heap[0]:
                heapq.heappush(self.left_heap, -num)
            else:
                max_num = heapq.heappushpop(self.right_heap, num)
                heapq.heappush(self.left_heap, -max_num)
        elif len(self.left_heap) > len(self.right_heap):
            if num >= -self.left_heap[0]:
                heapq.heappush(self.right_heap, num)
            else:
                min_num = -heapq.heappushpop(self.left_heap, -num)
                heapq.heappush(self.right_heap, min_num)
        else:
            if (len(self.left_heap) > 0) and (num >= -self.left_heap[0]):
                heapq.heappush(self.right_heap, num)
            else:
                heapq.heappush(self.left_heap, -num)

    def findMedian(self):
        if len(self.left_heap) < len(self.right_heap):
            return float(self.right_heap[0])
        elif len(self.left_heap) > len(self.right_heap):
            return float(-self.left_heap[0])
        else:
            return (self.right_heap[0] - self.left_heap[0]) / 2.0

    def remove_num(self, num: int):
        def heap_remove(heap: list[int], num: int):
            heap.remove(num)
            heapq.heapify(heap)

        if (len(self.right_heap) == 0) or (num < self.right_heap[0]):
            heap_remove(self.left_heap, -num)
        else:
            heap_remove(self.right_heap, num)

    def findSlidingWindowMedian(self, nums: list[int], k: int):
        for num in nums[: k - 1]:
            self.insertNum(num)

        result: list[float] = []
        for i, num in enumerate(nums[k - 1 :]):
            self.insertNum(num)
            result.append(self.findMedian())
            num_to_remove = nums[i]
            self.remove_num(num_to_remove)
        return result

    def findNextInterval(self, intervals: list[Interval]):
        result = [-1] * len(intervals)
        min_starts = [(item.start, i) for i, item in enumerate(intervals)]
        heapq.heapify(min_starts)
        min_ends = [(item.end, i) for i, item in enumerate(intervals)]
        heapq.heapify(min_ends)

        for _ in range(len(intervals)):
            end, end_idx = heapq.heappop(min_ends)
            while (len(min_starts) > 0) and (min_starts[0][0] < end):
                heapq.heappop(min_starts)
            if len(min_starts) == 0:
                break
            result[end_idx] = min_starts[0][1]
        return result

    def find_subsets(self, nums: list[int]):
        subsets: list[list[int]] = [[]]

        for num in nums:
            new_subsets = [list(subset) + [num] for subset in subsets]
            subsets.extend(new_subsets)
        return subsets

    def find_subsets_bit(self, nums: list[int]):
        return [
            [num for idx, num in enumerate(nums) if ((bit_map >> idx) & 1)]
            for bit_map in range(2 ** len(nums))
        ]

    def find_subsets_with_dup(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]

        subsets: list[list[int]] = [[], [nums[0]]]
        end_idx = 1
        for i, num in enumerate(nums[1:]):
            if num == nums[i]:
                new_subsets_idx = end_idx
            else:
                new_subsets_idx = 0
            end_idx = len(subsets)
            new_subsets = [
                list(subset) + [num] for subset in subsets[new_subsets_idx:]
            ]
            subsets.extend(new_subsets)
        return subsets

    def find_permutations(self, nums: list[int]):
        from collections import deque

        permutations: deque[list[int]] = deque([[]])
        for num in nums:
            n = len(permutations)
            for _ in range(n):
                permutation = permutations.popleft()
                for i in range(len(permutation) + 1):
                    new_permutation = permutation[:i] + [num] + permutation[i:]
                    permutations.append(new_permutation)
        return list(permutations)

    def find_letter_case_string_permutations(self, s: str):
        def swap_case(s: str, idx: int):
            return s[:idx] + s[idx].swapcase() + s[idx + 1 :]

        permutations: list[str] = [s]
        for i in range(len(s)):
            if s[i].isdigit():
                continue
            new_permutations = [
                swap_case(permutation, i) for permutation in permutations
            ]
            permutations.extend(new_permutations)
        return permutations

    def gen_valid_parentheses(self, num: int):
        result = ["()"]
        left_idx = 1
        for _ in range(num - 1):
            left = ["()" + s for s in result]
            two_side = ["(" + s + ")" for s in result]
            right = [s + "()" for s in result[left_idx:]]
            left_idx = len(left)
            result = left + two_side + right
        return result
