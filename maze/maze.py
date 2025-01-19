import sys
import random
import time
import copy
from typing import List, Tuple, Union

# using breadth-first search to find the shortest path from start to end of a maze

MazeType = List[List[str]]

maze: MazeType = [
    ['#', '#', '#', '#', 'x', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '#', 'o', '#'],
]

start_point: str = 'x'
end_point: str = 'o'


def print_maze(maze: MazeType) -> None:
    """Prints the maze to the console."""
    for row in maze:
        print(row)


def find_start_point(maze: MazeType) -> Tuple[int, int]:
    """Finds the start point in the maze.
    
    Args:
        maze: The maze represented as a list of lists.
    
    Returns:
        A tuple representing the row and column of the start point.
    """
    for i, row in enumerate(maze):
        if start_point in row:
            return i, row.index(start_point)
    raise ValueError("Start point not found in maze")


def find_end_point(maze: MazeType) -> Tuple[int, int]:
    """Finds the end point in the maze.
    
    Args:
        maze: The maze represented as a list of lists.
    
    Returns:
        A tuple representing the row and column of the end point.
    """
    for i, row in enumerate(maze):
        if end_point in row:
            return i, row.index(end_point)
    raise ValueError("End point not found in maze")


def find_neighbors(maze: MazeType, row: int, col: int) -> List[Tuple[int, int]]:
    """Finds the neighboring cells that can be visited.
    
    Args:
        maze: The maze represented as a list of lists.
        row: The current row of the cell.
        col: The current column of the cell.
    
    Returns:
        A list of tuples representing the neighboring cells.
    """
    neighbors = []
    if row > 0 and maze[row - 1][col] != '#':
        neighbors.append((row - 1, col))
    if row < len(maze) - 1 and maze[row + 1][col] != '#':
        neighbors.append((row + 1, col))
    if col > 0 and maze[row][col - 1] != '#':
        neighbors.append((row, col - 1))
    if col < len(maze[0]) - 1 and maze[row][col + 1] != '#':
        neighbors.append((row, col + 1))
    return neighbors


def find_path(maze: MazeType) -> List[Tuple[int, int]]:
    """Finds the path from start to end using breadth-first search.
    
    Args:
        maze: The maze represented as a list of lists.
    
    Returns:
        A list of tuples representing the path from start to end.
    """
    start_row, start_col = find_start_point(maze)
    end_row, end_col = find_end_point(maze)
    queue = [(start_row, start_col)]
    visited = []
    while queue:
        current_row, current_col = queue.pop(0)
        if (current_row, current_col) == (end_row, end_col):
            return visited
        visited.append((current_row, current_col))
        for neighbor in find_neighbors(maze, current_row, current_col):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
    return visited


def print_path(maze: MazeType, path: List[Tuple[int, int]]) -> None:
    """Prints the maze with the path marked.
    
    Args:
        maze: The maze represented as a list of lists.
        path: The path represented as a list of tuples.
    """
    for row, col in path:
        maze[row][col] = '*'
    print_maze(maze)


def main() -> None:
    """Main function to execute the maze pathfinding."""
    print_maze(maze)
    path = find_path(maze)
    print_path(maze, path)


if __name__ == '__main__':
    main()
