class Env:
    def __init__(self, goal_state=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """
        Initializing the puzzle
        """
        self.goal_state = goal_state
        self.size = 3  # 3x3 grid 

    def is_solvable(self, state):
        """
        Solvability Detection using inversion parity 
        """
        
        tiles = [t for t in state if t != 0]
        inversions = 0
        
        for i in range(len(tiles)):
            for j in range(i + 1, len(tiles)):
                if tiles[i] > tiles[j]:
                    inversions += 1
        
        
        return inversions % 2 == 0

    def get_actions(self, state):
        """
        Defines valid actions
        """
        actions = []
        blank_idx = state.index(0)
        row, col = divmod(blank_idx, self.size)

        # Action: Up 
        if row > 0: actions.append("Up")
        # Action: Down 
        if row < self.size - 1: actions.append("Down")
        # Action: Left 
        if col > 0: actions.append("Left")
        # Action: Right 
        if col < self.size - 1: actions.append("Right")
        
        return actions

    def get_successor(self, state, action):
        """
        Transition Model T(s, a) = s'
        """
        state_list = list(state)
        blank_idx = state_list.index(0)
        
        if action == "Up":
            target_idx = blank_idx - self.size
        elif action == "Down":
            target_idx = blank_idx + self.size
        elif action == "Left":
            target_idx = blank_idx - 1
        elif action == "Right":
            target_idx = blank_idx + 1
        
        # Perform swap [cite: 1265-1266, 1314]
        state_list[blank_idx], state_list[target_idx] = state_list[target_idx], state_list[blank_idx]
        return tuple(state_list)

    def goal_test(self, state):
        """
        Goal Test: Goal(s) = True if s is the goal configuration 
        """
        return state == self.goal_state