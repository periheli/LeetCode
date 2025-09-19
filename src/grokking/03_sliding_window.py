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
    def find_max_sum_sub_array(self, k: int, arr: list[int]) -> int:
        n = len(arr)
        window_sum = sum(arr[0:k])
        start = 0
        max_sum = window_sum
        for end in range(k, n):
            window_sum += arr[end] - arr[start]
            start += 1
            max_sum = max(max_sum, window_sum)
        return max_sum

    def find_min_sub_array(self, s: int, arr: list[int]) -> int:
        min_len = math.inf
        window_sum = 0
        start = 0
        for end in range(len(arr)):
            window_sum += arr[end]
            while window_sum >= s:
                min_len = min(min_len, end - start + 1)
                window_sum -= arr[start]
                start += 1
        return 0 if min_len == math.inf else min_len

    def find_length(self, str1: str, k: int) -> int:
        max_len = 0
        start = 0
        counter = {}
        for end in range(len(str1)):
            counter[str1[end]] = counter.get(str1[end], 0) + 1
            while len(counter) > k:
                counter[str1[start]] -= 1
                if counter[str1[start]] == 0:
                    del counter[str1[start]]
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len

    def find_length2(self, fruits: list[str]) -> int:
        max_len = 0
        start = 0
        counter = {}
        for end in range(len(fruits)):
            counter[fruits[end]] = counter.get(fruits[end], 0) + 1
            while len(counter) > 2:
                counter[fruits[start]] -= 1
                if counter[fruits[start]] == 0:
                    del counter[fruits[start]]
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len

    def find_length3(self, str1: str, k: int) -> int:
        max_len = 0
        start = 0
        mode_len = 0
        counter = {}
        for end in range(len(str1)):
            counter[str1[end]] = counter.get(str1[end], 0) + 1
            mode_len = max(mode_len, counter[str1[end]])
            # use if instead of while
            # - always keep the window size as max_len
            # - if not meet the condition, then the window will be extended
            if ((end - start + 1) - mode_len) > k:
                counter[str1[start]] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len

    def find_length4(self, arr: list[int], k: int) -> int:
        mex_len = 0
        start = 0
        zero_counter = 0
        for end in range(len(arr)):
            zero_counter += arr[end] == 0
            if zero_counter > k:
                zero_counter -= arr[start] == 0
                start += 1
            else:
                mex_len = max(mex_len, end - start + 1)
        return mex_len

    def find_permutation(self, str1: str, pattern: str) -> bool:
        from collections import Counter

        pattern_counter = Counter(pattern)
        start = 0
        counter = {}
        for end in range(len(str1)):
            end_char = str1[end]
            if end_char not in pattern_counter.keys():
                counter.clear()
                start = end + 1
                continue
            counter[end_char] = counter.get(end_char, 0) + 1
            while counter[end_char] > pattern_counter[end_char]:
                start_char = str1[start]
                counter[start_char] -= 1
                if counter[start_char] == 0:
                    del counter[start_char]
                start += 1
            if (end - start + 1) == len(pattern):
                return True
        return False

    def find_permutation2(self, str1: str, pattern: str) -> bool:
        from collections import Counter

        pattern_counter = Counter(pattern)
        matched = 0
        w = len(pattern)
        for i in range(len(str1)):
            end_char = str1[i]
            if end_char in pattern_counter:
                pattern_counter[end_char] -= 1
                matched += pattern_counter[end_char] == 0

            if i >= w:
                start_char = str1[i - w]
                if start_char in pattern_counter:
                    matched -= pattern_counter[start_char] == 0
                    pattern_counter[start_char] += 1

            if matched == len(pattern_counter):
                return True
        return False

    def find_string_anagrams(self, str1: str, pattern: str) -> list[int]:
        from collections import Counter

        pattern_counter = Counter(pattern)
        matched = 0
        start = 0
        result = []
        w = len(pattern)
        for end in range(len(str1)):
            end_char = str1[end]
            if end_char in pattern_counter:
                pattern_counter[end_char] -= 1
                matched += pattern_counter[end_char] == 0

            if end >= w:
                start_char = str1[start]
                if start_char in pattern_counter:
                    matched -= pattern_counter[start_char] == 0
                    pattern_counter[start_char] += 1
                start += 1

            if matched == len(pattern_counter):
                result.append(start)

        return result

    def find_sub_string(self, str1: str, pattern: str) -> str:
        from collections import Counter

        pattern_counter = Counter(pattern)
        start = 0
        matched = 0
        w = len(pattern_counter)
        min_len = len(str1) + 1
        sub_str_start = 0
        for end in range(len(str1)):
            end_char = str1[end]
            if end_char in pattern_counter:
                pattern_counter[end_char] -= 1
                matched += pattern_counter[end_char] == 0

            while matched == w:
                if (end - start + 1) < min_len:
                    min_len = end - start + 1
                    sub_str_start = start
                start_char = str1[start]
                if start_char in pattern_counter:
                    matched -= pattern_counter[start_char] == 0
                    pattern_counter[start_char] += 1
                start += 1
        if min_len == (len(str1) + 1):
            return ""
        return str1[sub_str_start : sub_str_start + min_len]

    def find_word_concatenation(self, str1: str, words: list[str]) -> list[int]:
        word_set = set(words)
        n_words = len(words)
        word_len = len(words[0])
        start = 0
        result = []
        for i in range(word_len):
            counter = {}
            start = i
            for end in range(i, len(str1) - word_len + 1, word_len):
                end_word = str1[end : end + word_len]
                if end_word in word_set:
                    counter[end_word] = counter.get(end_word, 0) + 1
                if (end - start) // word_len == n_words:
                    start_word = str1[start : start + word_len]
                    if start_word in word_set:
                        counter[start_word] -= 1
                        if counter[start_word] == 0:
                            del counter[start_word]
                    start += word_len
                if len(counter) == n_words:
                    result.append(start)
        return result

    def find_sub_arrays(self, nums: list[int], target: int) -> int:
        if target <= 1:
            return 0

        count = 0
        product = 1
        start = 0
        for end in range(len(nums)):
            product *= nums[end]
            while product >= target:
                product //= nums[start]
                start += 1
            count += end - start + 1
        return count

    def find_sub_arrays(self, nums: list[int], target: int) -> list[list[int]]:
        if target <= 1:
            return []

        sub_arrs = []
        acc_product = 1
        start = 0
        for end in range(len(nums)):
            acc_product *= nums[end]
            while acc_product >= target:
                acc_product //= nums[start]
                start += 1
            # for i in range(start, end + 1):
            for i in range(end, start - 1, -1):
                sub_arrs.append(nums[i : end + 1])
        return sub_arrs
