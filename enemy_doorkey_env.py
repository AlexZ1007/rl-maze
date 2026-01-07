import random
from minigrid.envs.doorkey import DoorKeyEnv
from minigrid.core.world_object import Ball

class DoorKeyWithEnemyEnv(DoorKeyEnv):
    """
    DoorKey + a single randomly-moving enemy (red ball).
    If the agent touches the enemy -> episode ends with reward -1.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.enemy_pos = None
        self.enemy_obj = Ball("red")

    def _gen_grid(self, width, height):
        super()._gen_grid(width, height)

        # Place enemy on an empty cell, but avoid agent start area and important objects
        self.enemy_pos = self._place_enemy_safely()

    def _place_enemy_safely(self):
        # Collect forbidden positions: agent, key, door, goal
        forbidden = set()
        forbidden.add(tuple(self.agent_pos))

        for j in range(self.height):
            for i in range(self.width):
                obj = self.grid.get(i, j)
                if obj is None:
                    continue
                if obj.type in ("key", "door", "goal"):
                    forbidden.add((i, j))

        # Try random empty spots
        for _ in range(200):
            x = random.randint(1, self.width - 2)
            y = random.randint(1, self.height - 2)
            if (x, y) in forbidden:
                continue
            if self.grid.get(x, y) is None:
                self.grid.set(x, y, self.enemy_obj)
                return (x, y)

        # Fallback: just place normally (very unlikely to reach here)
        pos = self.place_obj(self.enemy_obj)
        return pos

    def step(self, action):
        # 1) agent acts first
        obs, reward, terminated, truncated, info = super().step(action)

        # 2) enemy moves after agent
        self._move_enemy()

        # 3) collision check
        if tuple(self.agent_pos) == tuple(self.enemy_pos):
            terminated = True
            reward = -1.0

        return obs, reward, terminated, truncated, info

    def _move_enemy(self):
        if self.enemy_pos is None:
            return

        x, y = self.enemy_pos

        moves = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]
        dx, dy = random.choice(moves)
        nx, ny = x + dx, y + dy

        # bounds
        if not (0 <= nx < self.width and 0 <= ny < self.height):
            return

        # only move into empty cells (do not overwrite key/door/goal/walls)
        if self.grid.get(nx, ny) is None:
            self.grid.set(x, y, None)
            self.enemy_pos = (nx, ny)
            self.grid.set(nx, ny, self.enemy_obj)
