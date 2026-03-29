from environment import Env
from solver import AStarSolver, BFSSolver, DFSSolver

def get_input():
    n = int(input())
    initial = []
    for i in range(n):
        row = list(map(int, input().split()))
        initial.append(row)
    return initial
