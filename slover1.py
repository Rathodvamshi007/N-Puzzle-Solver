from collections import deque
import time

class BFSSolver:
    def __init__(self, environment):
        self.env = environment
        
        self.nodes_expanded = 0
        self.max_frontier_size = 0
        self.execution_time = 0

    def solve(self, start_state):
        start_time = time.time()

        frontier = deque([(start_state, [start_state])])  # (state, path)
        explored = set([start_state])

        self.nodes_expanded = 0
        self.max_frontier_size = 1

        while frontier:
            self.max_frontier_size = max(self.max_frontier_size, len(frontier))

            current_state, path = frontier.popleft()
            self.nodes_expanded += 1

            if self.env.goal_test(current_state):
                self.execution_time = time.time() - start_time
                return path, self.nodes_expanded, self.max_frontier_size, self.execution_time

            for action in self.env.get_actions(current_state):
                neighbor = self.env.get_successor(current_state, action)

                if neighbor not in explored:
                    explored.add(neighbor)
                    frontier.append((neighbor, path + [neighbor]))

        self.execution_time = time.time() - start_time
        return None, self.nodes_expanded, self.max_frontier_size, self.execution_time
