#!/usr/bin/python3
import sys

def solve_nqueens(n):
    def can_place(pos, ocuppied_positions):
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
                ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
                ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                return False
        return True

    def place_queens(n, index, ocuppied_positions, result):
        if index == n:
            result.append(ocuppied_positions[:])
            return
        for i in range(n):
            if can_place(i, ocuppied_positions):
                ocuppied_positions.append(i)
                place_queens(n, index + 1, ocuppied_positions, result)
                ocuppied_positions.pop()

    result = []
    place_queens(n, 0, [], result)
    return result

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    result = solve_nqueens(n)
    for solution in result:
        formatted_solution = [[i, pos] for i, pos in enumerate(solution)]
        print(formatted_solution)

if __name__ == "__main__":
    main()
