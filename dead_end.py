#!/usr/bin/env python3
import sys
import collections


def getboard(maze):
    f = open(maze, "r")
    data = f.read()
    data = data.split("\n")
    return data


def getPositionOfGate(maze):
    gate = []
    if " " in maze[0]:
        gate.append([maze[0].index(" "), 0])
    if " " in maze[len(maze)-1]:
        gate.append([maze[len(maze)-1].index(" "), len(maze)-1])
    for y in range(len(maze)):
        if maze[y][0] == " ":
            gate.append([0, y])
        if maze[y][len(maze[y])-1] == " ":
            gate.append([len(maze[y])-1, y])
    return gate


def bfs(maze, start, end):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if [x, y] == end:
            path.append([path[0][0], path[0][1]])
            path.remove(path[0])
            return path
        for x2, y2 in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
            if maze[y2][x2] == ' ' and (x2, y2) not in seen:
                    queue.append(path + [[x2, y2]])
                    seen.add((x2, y2))
    return None


def getResult(maze, move):
    result = []
    for i in range(len(maze)):
        result.append([maze[i][0]])
        for j in range(len(maze[0])):
            result[i].append(maze[i][j])
    for i in range(len(result)):
        for j in range(len(result[0])):
            if [j, i] in move:
                result[i][j] = ' '
            else:
                result[i][j] = '*'
        result[i] = "".join(result[i])
    return result


def main():
    maze = getboard(sys.argv[-1])
    gate = getPositionOfGate(maze)
    move = bfs(maze, (gate[0][0], gate[0][1]), gate[1])
    print(move)
    maze = getResult(maze, move)
    print("\n".join(maze))


if __name__ == '__main__':
    main()
