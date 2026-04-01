from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)

        robots = [[positions[i], healths[i], directions[i], i] for i in range(n)]
        

        robots.sort(key=lambda x: x[0])
        
        stack = []
        
        for robot in robots:
            pos, health, direction, orig_idx = robot
            
            if direction == 'R':

                stack.append(robot)
            else:

                survived = True
                while stack and stack[-1][2] == 'R':
                    r_health = stack[-1][1]
                    
                    if r_health > health:

                        stack[-1][1] -= 1
                        survived = False
                        break
                    elif r_health < health:

                        stack.pop()
                        health -= 1
                    else:

                        stack.pop()
                        survived = False
                        break
                
                if survived:
                    robot[1] = health
                    stack.append(robot)
                    

        stack.sort(key=lambda x: x[3])
        

        return [robot[1] for robot in stack]
        