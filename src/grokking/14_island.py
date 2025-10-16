class Solution:
    def count_islands(self, matrix: list[list[int]]) -> int:
        from collections import deque

        n, m = len(matrix), len(matrix[0])
        visited = [[False] * m for _ in range(n)]

        def expand_island(i: int, j: int):
            queue = deque([(i, j)])
            while queue:
                row, col = queue.popleft()
                if row < 0 or row >= n or col < 0 or col >= m:
                    continue
                if visited[row][col] or (not matrix[row][col]):
                    continue

                visited[row][col] = True
                queue.append((row + 1, col))
                queue.append((row - 1, col))
                queue.append((row, col + 1))
                queue.append((row, col - 1))

        counter = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] and (not visited[i][j]):
                    counter += 1
                    expand_island(i, j)
        return counter

    def max_area_of_island(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        def find_area(row: int, col: int) -> int:
            if row < 0 or row >= n or col < 0 or col >= m:
                return 0
            if matrix[row][col] == 0:
                return 0

            matrix[row][col] = 0
            area = 1
            area += find_area(row + 1, col)
            area += find_area(row - 1, col)
            area += find_area(row, col + 1)
            area += find_area(row, col - 1)
            return area

        max_area = 0
        for row in range(n):
            for col in range(m):
                area = find_area(row, col)
                max_area = max(area, max_area)
        return max_area

    def flood_fill(
        self, matrix: list[list[int]], x: int, y: int, new_color: int
    ):
        n, m = len(matrix), len(matrix[0])

        def helper(x: int, y: int, old_color: int):
            if x < 0 or x >= n or y < 0 or y >= m:
                return 0
            if matrix[x][y] != old_color:
                return 0

            matrix[x][y] = new_color
            helper(x + 1, y, old_color)
            helper(x - 1, y, old_color)
            helper(x, y + 1, old_color)
            helper(x, y - 1, old_color)

        if matrix[x][y] != new_color:
            helper(x, y, matrix[x][y])
        return matrix

    def count_closed_islands(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        counter = 0

        def is_closed(row: int, col: int) -> bool:
            if row < 0 or row >= n or col < 0 or col >= m:
                return False
            if matrix[row][col] == 0:
                return True

            matrix[row][col] = 0
            closed = True
            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if not is_closed(row + i, col + j):
                    closed = False
            return closed

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    counter += is_closed(i, j)
        return counter

    def find_island_perimeter(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        visited = [[False] * m for _ in range(n)]

        def find_perimeter(row: int, col: int) -> int:
            if row < 0 or row >= n or col < 0 or col >= m:
                return 1
            if visited[row][col]:
                return 0
            if matrix[row][col] == 0:
                return 1
            count = 0
            visited[row][col] = True
            count += find_perimeter(row + 1, col)
            count += find_perimeter(row - 1, col)
            count += find_perimeter(row, col + 1)
            count += find_perimeter(row, col - 1)
            return count

        for i in range(n):
            for j in range(m):
                if matrix[i][j]:
                    return find_perimeter(i, j)
        return 0

    def find_distinct_islands(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        def island_shape(row: int, col: int) -> list[int] | None:
            if row < 0 or row >= n or col < 0 or col >= m:
                return None
            if matrix[row][col] == 0:
                return None

            matrix[row][col] = 0
            parent_shape = 0
            child_shapes: list[int] = []
            for idx, (i, j) in enumerate([(1, 0), (-1, 0), (0, 1), (0, -1)]):
                child = island_shape(row + i, col + j)
                if child is not None:
                    parent_shape += 2**idx
                    child_shapes.extend(child)
            return [parent_shape] + child_shapes

        shape_set = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    shape_set.add(tuple(island_shape(i, j)))
        return len(shape_set)

    def find_distinct_islands(self, matrix: list[list[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        def island_shape(row: int, col: int) -> str:
            if row < 0 or row >= n or col < 0 or col >= m:
                return ""
            if matrix[row][col] == 0:
                return ""

            matrix[row][col] = 0
            parent_shape = ""
            for i, j, dir in [
                (1, 0, "D"),
                (-1, 0, "U"),
                (0, 1, "R"),
                (0, -1, "L"),
            ]:
                child = island_shape(row + i, col + j)
                if len(child) > 0:
                    parent_shape += dir + child
            return parent_shape + "B"

        shape_set: set[str] = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    shape_set.add(island_shape(i, j))
        return len(shape_set)

    def has_cycle(self, matrix: list[list[str]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        visited = [[False] * m for _ in range(n)]

        def is_cycle(row: int, col: int, char: str, last_dir: int) -> bool:
            if row < 0 or row >= n or col < 0 or col >= m:
                return False
            if matrix[row][col] != char:
                return False
            if visited[row][col]:
                return True

            visited[row][col] = True
            for dir, (i, j) in enumerate([(1, 0), (0, 1), (0, -1), (-1, 0)]):
                if (dir + last_dir) == 3:
                    continue
                if is_cycle(row + i, col + j, char, dir):
                    return True
            return False

        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    if is_cycle(i, j, matrix[i][j], 4):
                        return True
        return False
