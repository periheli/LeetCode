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
from turtle import left
from typing import Dict, List, Optional, Set, Tuple

from sortedcontainers import SortedList


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Job:
    def __init__(self, start: int, end: int, cpu_load: int):
        self.start = start
        self.end = end
        self.cpuLoad = cpu_load


class Solution:
    def merge(self, intervals: list[Interval]) -> list[Interval]:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        merged_intervals: list[Interval] = []
        for interval in sorted_intervals:
            if (
                not merged_intervals
                or merged_intervals[-1].end < interval.start
            ):
                merged_intervals.append(interval)
            else:
                merged_intervals[-1].end = max(
                    merged_intervals[-1].end, interval.end
                )
        return merged_intervals

    def merge_create_new(self, intervals: list[Interval]) -> list[Interval]:
        if not intervals:
            return []
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        merged_intervals: list[Interval] = []
        start, end = sorted_intervals[0].start, sorted_intervals[0].end
        for interval in sorted_intervals[1:]:
            if interval.start <= end:
                end = max(end, interval.end)
            else:
                merged_intervals.append(Interval(start, end))
                start, end = interval.start, interval.end
        merged_intervals.append(Interval(start, end))
        return merged_intervals

    def insert(
        self, intervals: list[Interval], new_interval: Interval
    ) -> list[Interval]:
        if not intervals:
            return [new_interval]
        start_idx = bisect.bisect_left(
            intervals,
            new_interval.start,
            key=lambda x: x.end,
        )
        merged_intervals = intervals[:start_idx]
        end_idx = start_idx
        new_start, new_end = new_interval.start, new_interval.end
        for interval in intervals[start_idx:]:
            if interval.start <= new_interval.end:
                end_idx += 1
                new_start = min(new_start, interval.start)
                new_end = max(new_end, interval.end)
            else:
                break
        merged_intervals.append(Interval(new_start, new_end))
        merged_intervals.extend(intervals[end_idx:])
        return merged_intervals

    def intersect(
        self, intervals_a: list[Interval], intervals_b: list[Interval]
    ) -> list[Interval]:
        def _intersect(
            interval_a: Interval, interval_b: Interval
        ) -> Optional[Interval]:
            start = max(interval_a.start, interval_b.start)
            end = min(interval_a.end, interval_b.end)
            if start <= end:
                return Interval(start, end)
            return None

        result: list[Interval] = []
        i, j = 0, 0
        while i < len(intervals_a) and j < len(intervals_b):
            interval_a = intervals_a[i]
            interval_b = intervals_b[j]
            intersection = _intersect(interval_a, interval_b)
            if intersection is not None:
                result.append(intersection)
            if interval_a.end < interval_b.end:
                i += 1
            elif interval_a.end > interval_b.end:
                j += 1
            else:
                i += 1
                j += 1
        return result

    def can_attend_all_appointments(self, intervals: list[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        for i in range(1, len(sorted_intervals)):
            if sorted_intervals[i].start < sorted_intervals[i - 1].end:
                return False
        return True

    def find_minimum_meeting_rooms(self, intervals: list[Interval]) -> int:
        import heapq

        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        min_heap: list[int] = []
        min_rooms = 0
        for interval in sorted_intervals:
            while min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
            min_rooms = max(min_rooms, len(min_heap))
        return min_rooms

    def find_max_cpu_load(self, jobs: list[Job]) -> int:
        import heapq

        sorted_jobs = sorted(jobs, key=lambda x: x.start)
        max_cpu_load = 0
        curr_cpu_load = 0
        min_heap: list[Tuple[int, int]] = []  # (end, cpuLoad)
        for job in sorted_jobs:
            while min_heap and min_heap[0][0] <= job.start:
                ended_job = heapq.heappop(min_heap)
                curr_cpu_load -= ended_job[1]
            heapq.heappush(min_heap, (job.end, job.cpuLoad))
            curr_cpu_load += job.cpuLoad
            max_cpu_load = max(max_cpu_load, curr_cpu_load)
        return max_cpu_load

    def find_employee_free_time(
        self, schedule: list[list[Interval]]
    ) -> list[Interval]:
        import heapq

        free_times: list[Interval] = []
        min_heap: List[Tuple[int, int, int, int]] = [
            (emp[0].start, emp[0].end, 0, i) for i, emp in enumerate(schedule)
        ]
        heapq.heapify(min_heap)
        prev_end = min_heap[0][1]
        while len(min_heap) > 0:
            curr_start, curr_end, job_idx, emp_idx = min_heap[0]
            if curr_start > prev_end:
                free_times.append(Interval(prev_end, curr_start))
                prev_end = curr_end
            else:
                prev_end = max(prev_end, curr_end)
            if job_idx + 1 < len(schedule[emp_idx]):
                next_job = schedule[emp_idx][job_idx + 1]
                heapq.heapreplace(
                    min_heap,
                    (next_job.start, next_job.end, job_idx + 1, emp_idx),
                )
            else:
                heapq.heappop(min_heap)
        return free_times
