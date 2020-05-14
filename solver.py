import copy
import os
import time
from collections import deque

# Basic Operation is the reassignment(swap) in the
# sort() function, as it is used the most.
# Specific lines are: 115-152
# Example Lines:
#   temp = up[row + 1][col]
#   up[row + 1][col] = 'X'
#   up[row][col] = temp

runs = 0  # counts runs
basic_op = 0  # counts # of basic_op performed


class Solver:
    # Find Empty Space
    def empty_space(matrix, size):
        for row in range(size):
            for col in range(size):
                if matrix[row][col] == 'X':
                    return row, col

    # Read in the tile set
    def read_graph(filename):
        matrix = [[]]
        line = 0

        # Intake tile set
        with open(filename, 'r') as file:
            while line < file.__sizeof__():
                matrix[line] = file.readline().strip()

                if matrix[line].count('') == 1:
                    del matrix[line]
                    break
                else:
                    matrix.append([])
                line += 1

        # Split lines into individuals
        for row in range(len(matrix)):
            matrix[row] = matrix[row].split()

        # Convert to numbers
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if matrix[row][col] == 'X':
                    continue
                else:
                    matrix[row][col] = int(matrix[row][col])

        return matrix

    # Helper Functions
    @staticmethod
    def get_graph():
        for x in range(0, 3):
            if x == 0:
                path = "Puzzles_3/"
            elif x == 1:
                path = "Puzzles_8/"
            else:
                path = "Puzzles_15/"

            print("Selections for folder %s:\n" % path, os.listdir(path))

        filename = input("Select a graph: ")
        return filename

    def print_graph(matrix):
        for index in range(0, matrix.__len__()):
            print(matrix[index])

    # Still a God Sort (Main Sort Logic)
    def sort(matrix):
        global runs, basic_op

        # Hard Code a Solution rather than using above tile sorter function
        size = len(matrix)
        if size == 2:
            sorted_tile = [[1, 2], [3, 'X']]
        elif size == 3:
            sorted_tile = [[1, 2, 3], [4, 5, 6], [7, 8, 'X']]
        elif size == 4:
            sorted_tile = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 'X']]

        print("Solution Graph:")
        Solver.print_graph(sorted_tile)

        open_moves = deque([])
        open_moves.append(matrix)
        closed_moves = []

        while len(open_moves) > 0:
            current_matrix = open_moves.popleft()
            runs += 1
            print("------Matrix for step: %d------" % runs)
            Solver.print_graph(current_matrix)
            if current_matrix == sorted_tile:  # Solution Found, exit
                return sorted_tile

            elif runs > 25000:  # Laze way of killing unsolvable tiles
                print("Probably and unsolvable tile, exiting!")
                exit(1)

            else:  # Continue Searching for Solution
                up = copy.deepcopy(current_matrix)  # Makes Actual Copy of array, rather than pointer
                row, col = Solver.empty_space(up, len(up))
                if row + 1 < len(up):
                    basic_op += 1
                    # print("Up")
                    temp = up[row + 1][col]
                    up[row + 1][col] = 'X'
                    up[row][col] = temp
                    if up not in open_moves or closed_moves:
                        open_moves.append(up)

                down = copy.deepcopy(current_matrix)  # Makes Actual Copy of array, rather than pointer
                row, col = Solver.empty_space(down, len(down))
                if row - 1 >= 0:
                    basic_op += 1
                    # print("Down")
                    temp = down[row - 1][col]
                    down[row - 1][col] = 'X'
                    down[row][col] = temp
                    if down not in open_moves or closed_moves:
                        open_moves.append(down)

                left = copy.deepcopy(current_matrix)  # Makes Actual Copy of array, rather than pointer
                row, col = Solver.empty_space(left, len(left))
                if col - 1 >= 0:
                    basic_op += 1
                    # print("Left")
                    temp = left[row][col - 1]
                    left[row][col - 1] = 'X'
                    left[row][col] = temp
                    if left not in open_moves or closed_moves:
                        open_moves.append(left)

                right = copy.deepcopy(current_matrix)  # Makes Actual Copy of array, rather than pointer
                row, col = Solver.empty_space(right, len(right))
                if col + 1 < len(right[row]):
                    basic_op += 1
                    # print("Right")
                    temp = right[row][col + 1]
                    right[row][col + 1] = 'X'
                    right[row][col] = temp
                    if right not in open_moves or closed_moves:
                        open_moves.append(right)

            closed_moves.append(current_matrix)  # Save Latest Step

        return "No Solution, or Cyclical"


def main():
    filename = Solver.get_graph()
    matrix = Solver.read_graph(filename)

    print("Original Tile Set Below:")
    Solver.print_graph(matrix)
    time_start = time.time()
    Solver.sort(matrix)
    time_end = time.time()

    print("Time Taken: ", (time_end - time_start))
    print("Basic Operation Performed: %d" % basic_op)

    # Solver.solution(matrix)


if __name__ == "__main__":
    main()
