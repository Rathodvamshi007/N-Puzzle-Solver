from environment import Env
from solver import AStarSolver, BFSSolver, DFSSolver

def get_input():
    n = int(input())
    initial = []
    for i in range(n):
        row = list(map(int, input().split()))
        initial.append(row)
    return initial
def print_path(path):
    for step in path:
        for row in step:
            print(row)
        print()
def main():
    initial = get_input()
    puzzle = Env(initial)

    choice = int(input())

    if choice == 1:
        solver = AStarSolver(puzzle)
    elif choice == 2:
        solver = BFSSolver(puzzle)
    elif choice == 3:
        solver = DFSSolver(puzzle)
    else:
        return
    path = solver.solve()
if path:
        print(len(path) - 1)
        print_path(path)
    else:
        print("No solution")
