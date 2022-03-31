# using breadth first search to find the shortest path from start to end
# of a maze


import sys
import random
import time
import copy


maze = [
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

start_point = 'x'
end_point = 'o'


def print_maze(maze):
    for row in maze:
        print(row)


def find_start_point(maze):
    for i, row in enumerate(maze):
        if start_point in row:
            return i, row.index(start_point)


def find_end_point(maze):
    for i, row in enumerate(maze):
        if end_point in row:
            return i, row.index(end_point)


def find_neighbors(maze, row, col):
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


def find_path(maze):
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


def print_path(maze, path):
    for row, col in path:
        maze[row][col] = '*'
    print_maze(maze)




def main():
    print_maze(maze)
    path = find_path(maze)
    print_path(maze, path)


if __name__ == '__main__':
    main()