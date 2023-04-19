class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        start_row, start_col = entrance
        maze[start_row][start_col] = '+'
        q = collections.deque([(start_row, start_col, 0)])
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        while q:
            x, y, d = q.popleft()
            maze[x][y] = '+'
            for dx, dy in directions:
                next_x, next_y = x + dx, y + dy
                if 0 <= next_x < len(maze) and 0 <= next_y < len(maze[0]):
                    if maze[next_x][next_y] == '.':
                        if next_x == 0 or next_x == len(maze) - 1 or next_y == 0 or next_y == len(maze[0]) - 1:
                            return d + 1
                        maze[next_x][next_y] = '+'
                        q.append((next_x, next_y, d + 1))

        return -1
