from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        # Total steps to make one full loop around the perimeter
        self.perimeter = 2 * width + 2 * height - 4
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> List[int]:
        # Origin
        if self.pos == 0:
            return [0, 0]
        # Bottom Edge (Moving East)
        elif self.pos < self.w:
            return [self.pos, 0]
        # Right Edge (Moving North)
        elif self.pos < self.w + self.h - 1:
            return [self.w - 1, self.pos - self.w + 1]
        # Top Edge (Moving West)
        elif self.pos < 2 * self.w + self.h - 2:
            return [2 * self.w + self.h - 3 - self.pos, self.h - 1]
        # Left Edge (Moving South)
        else:
            return [0, 2 * self.w + 2 * self.h - 4 - self.pos]

    def getDir(self) -> str:
        # Origin Exception: Faces South if it wrapped entirely around, East if newly initialized
        if self.pos == 0:
            return "South" if self.moved else "East"
        # Bottom Edge
        elif self.pos < self.w:
            return "East"
        # Right Edge
        elif self.pos < self.w + self.h - 1:
            return "North"
        # Top Edge
        elif self.pos < 2 * self.w + self.h - 2:
            return "West"
        # Left Edge
        else:
            return "South"

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()