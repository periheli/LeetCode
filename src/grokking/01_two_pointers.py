# pyright: reportRedeclaration=false
import bisect
from collections import deque
from typing import List, Set, Tuple


class Solution:
    # Pair with Target Sum
    # 167. Two Sum II - Input Array Is Sorted
    def search(self, arr, target_sum):
        left, right = 0, len(arr) - 1
        while left < right:
            two_sum = arr[left] + arr[right]
            if two_sum == target_sum:
                return [left, right]
            elif two_sum < target_sum:
                left += 1
            else:
                right += 1

        return [-1, -1]

    # Find Non-Duplicate Number Instances
    # 26. Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums: List[int]) -> int:
        nunique = 0
        for num in nums[1:]:
            if num != nums[nunique]:
                nunique += 1
                nums[nunique] = num
        return nunique + 1

    # 977. Squares of a Sorted Array
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[right] ** 2 > nums[left] ** 2:
                res[right - left] = nums[right] ** 2
                right -= 1
            else:
                res[right - left] = nums[left] ** 2
                left += 1
        res[0] = nums[left] ** 2
        return res

    # Triplet Sum to Zero
    # 15. 3Sum
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)

        def two_sum(nums: List[int], target: int) -> Set[Tuple[int, int]]:
            left, right = 0, len(nums) - 1
            pair_set = set()
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    pair_set.add((nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1
            return pair_set

        triplet_list = []
        for i, num in enumerate(sorted_nums[:-2]):
            if num > 0:
                break
            if i > 0 and num == sorted_nums[i - 1]:
                continue
            triplet_list.extend(
                [
                    [num, pair[0], pair[1]]
                    for pair in two_sum(sorted_nums[i + 1 :], -num)
                ]
            )
        return triplet_list

    # Triplet Sum Close to Target
    # 16. 3Sum Closest
    closest_num: int

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        sorted_nums = sorted(nums)
        self.closest_num = sum(sorted_nums[:3])

        def two_sum(nums: List[int], fixed_num: int):
            left, right = 0, len(nums) - 1
            while left < right:
                three_sum = fixed_num + nums[left] + nums[right]
                if three_sum == target:
                    return True
                if three_sum < target:
                    left += 1
                else:
                    right -= 1
                if abs(target - self.closest_num) > abs(target - three_sum):
                    self.closest_num = three_sum
                elif abs(target - self.closest_num) == abs(target - three_sum):
                    self.closest_num = min(self.closest_num, three_sum)
            return False

        for i, num in enumerate(sorted_nums[:-2]):
            if two_sum(sorted_nums[i + 1 :], num):
                return target

        return self.closest_num

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        sorted_nums = sorted(nums)
        closest_num = sum(sorted_nums[:3])

        for i, num in enumerate(sorted_nums[:-2]):
            left, right = i + 1, n - 1
            while left < right:
                three_sum = num + sorted_nums[left] + sorted_nums[right]
                if three_sum == target:
                    return target

                if three_sum < target:
                    left += 1
                else:
                    right -= 1

                if abs(target - closest_num) > abs(target - three_sum):
                    closest_num = three_sum
                elif abs(target - closest_num) == abs(target - three_sum):
                    closest_num = min(closest_num, three_sum)

        return closest_num

    # Triplets with Smaller Sum
    def searchTriplets(self, arr, target):
        sorted_nums = sorted(arr)

        def count_pair(nums: List[int], max_num: int):
            count = 0
            left, right = 0, len(nums) - 1
            while left < right:
                while left < right and nums[left] + nums[right] < max_num:
                    left += 1
                count += left
                right -= 1
            return count + right * (right + 1) // 2

        return sum(
            count_pair(sorted_nums[i + 1 :], target - num)
            for i, num in enumerate(sorted_nums[:-2])
        )

    # Dutch National Flag
    def sortColors(self, nums: List[int]) -> None:
        left_most_one, left_most_two = 0, 0
        for i, num in enumerate(nums):
            if num == 0:
                nums[i], nums[left_most_two] = nums[left_most_two], nums[i]
                nums[left_most_two], nums[left_most_one] = (
                    nums[left_most_one],
                    nums[left_most_two],
                )
                left_most_one += 1
                left_most_two += 1
            elif num == 1:
                nums[i], nums[left_most_two] = nums[left_most_two], nums[i]
                left_most_two += 1

    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                mid += 1

    def compare(self, str1: str, str2: str) -> bool:
        idx1 = len(str1) - 1
        idx2 = len(str2) - 1
        counter1 = counter2 = 0
        while True:
            while idx1 >= 0 and (counter1 > 0 or str1[idx1] == "#"):
                counter1 += 1 if str1[idx1] == "#" else -1
                idx1 -= 1
            while idx2 >= 0 and (counter2 > 0 or str2[idx2] == "#"):
                counter2 += 1 if str2[idx2] == "#" else -1
                idx2 -= 1
            if idx1 < 0 and idx2 < 0:
                return True
            if idx1 < 0 or idx2 < 0:
                return False
            if idx1 >= 0 and idx2 >= 0 and str1[idx1] != str2[idx2]:
                return False
            idx1 -= 1
            idx2 -= 1

    def compare_stream(self, str1: str, str2: str) -> bool:
        def build(s: str):
            stack = deque()
            for c in s:
                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)

        return build(str1) == build(str2)

    # 581. Shortest Unsorted Continuous Subarray
    def sort(self, arr: List[int]) -> int:
        n = len(arr)
        max_idx_left = 0
        while (
            max_idx_left < n - 1 and arr[max_idx_left] <= arr[max_idx_left + 1]
        ):
            max_idx_left += 1
        if max_idx_left == n - 1:
            return 0
        min_idx_right = n - 1
        while (
            min_idx_right > 0 and arr[min_idx_right] >= arr[min_idx_right - 1]
        ):
            min_idx_right -= 1

        sub_arr_min = min(arr[max_idx_left : min_idx_right + 1])
        sub_arr_max = max(arr[max_idx_left : min_idx_right + 1])

        sub_arr_start = bisect.bisect_right(
            arr, sub_arr_min, 0, max_idx_left + 1
        )
        sub_arr_end = bisect.bisect_left(arr, sub_arr_max, min_idx_right, n)

        return sub_arr_end - sub_arr_start

    def sort_1path(self, arr: List[int]) -> int:
        n = len(arr)
        max_idx_left = 0
        while (
            max_idx_left < n - 1 and arr[max_idx_left] <= arr[max_idx_left + 1]
        ):
            max_idx_left += 1
        if max_idx_left == n - 1:
            return 0

        min_right = arr[max_idx_left + 1]
        max_right = arr[max_idx_left]
        sub_arr_end = max_idx_left + 1
        for i in range(max_idx_left + 1, n):
            min_right = min(min_right, arr[i])
            max_right = max(max_right, arr[i])
            if arr[i] < max_right:
                sub_arr_end = i + 1
        sub_arr_start = bisect.bisect_right(arr, min_right, 0, max_idx_left + 1)
        return sub_arr_end - sub_arr_start
