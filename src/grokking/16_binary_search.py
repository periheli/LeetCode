from typing import Protocol


class Stream(Protocol):
    def get(self, index: int) -> int:
        """"""
        ...


class Solution:
    def ceil(self, arr: list[int], key: int) -> int:
        lo, hi = 0, len(arr) - 1
        if arr[hi] < key:
            return -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def bisect_right(self, arr: list[int], key: int) -> int:
        # default bisect
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] <= key:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    def floor(self, arr: list[int], key: int) -> int:
        lo, hi = 0, len(arr) - 1
        if arr[lo] > key:
            return -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                hi = mid - 1
            else:
                lo = mid + 1
        return hi

    def find_range(self, arr: list[int], key: int):
        # bisect_right
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] <= key:
                lo = mid + 1
            else:
                hi = mid - 1
        end = lo
        if arr[end - 1] != key:
            return [-1, -1]
        # bisect_left
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] >= key:
                hi = mid - 1
            else:
                lo = mid + 1
        start = lo
        return [start, end - 1]

    def search_infinite(self, reader: Stream, key: int) -> int:
        hi = 1
        while reader.get(hi) < key:
            hi *= 2
        lo = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if reader.get(mid) == key:
                return mid
            elif reader.get(mid) > key:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

    def find_max(self, arr: list[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] > arr[mid + 1]:
                hi = mid
            else:
                lo = mid + 1
        return arr[lo]

    def search_rotated(self, arr: list[int], key: int) -> int:
        def binary(lo: int, hi: int):
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] == key:
                    return mid
                elif arr[mid] > key:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1

        if arr[0] <= arr[-1]:
            return binary(0, len(arr) - 1)

        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid + 1] <= arr[hi]:
                hi = mid
            else:
                lo = mid + 1
            if arr[lo] < arr[hi]:
                lo = hi
        max_idx = lo
        left_res = binary(0, max_idx)
        if left_res == -1:
            return binary(max_idx + 1, len(arr) - 1)
        return left_res
