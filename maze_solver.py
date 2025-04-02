class MazeSolver:
    def __init__(self, maze, start, target):
        self.maze = maze
        self.start = start
        self.target = target
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]  # Down, Right, Left, Up

    def dls(self, x, y, depth, max_depth, path, visited):
        """ Depth-Limited Search (DLS) used in IDDFS """
        if depth > max_depth:
            return False
        if (x, y) == self.target:
            path.append((x, y))
            return True

        visited.add((x, y))
        path.append((x, y))

        for dx, dy in self.directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.maze[nx][ny] == 0 and (nx, ny) not in visited:
                if self.dls(nx, ny, depth + 1, max_depth, path, visited):
                    return True

        path.pop()  # Backtrack if no valid path found
        return False

    def iddfs(self, max_depth):
        """ Iterative Deepening DFS (IDDFS) """
        for depth in range(max_depth + 1):
            path = []
            visited = set()
            if self.dls(self.start[0], self.start[1], 0, depth, path, visited):
                print(f"Path found at depth {depth} using IDDFS")
                print(f"Traversal Order: {path}")
                return
        print(f"Path not found at max depth {max_depth} using IDDFS")


def get_input():
    """ Reads input in the exact format provided """
    rows, cols = map(int, input().strip().split())

    maze = []
    for _ in range(rows):
        maze.append(list(map(int, input().strip().split())))

    start_x, start_y = map(int, input().strip().split()[1:])
    target_x, target_y = map(int, input().strip().split()[1:])

    return maze, (start_x, start_y), (target_x, target_y)


if __name__ == "__main__":
    maze, start, target = get_input()

    solver = MazeSolver(maze, start, target)
    solver.iddfs(max_depth=6)
