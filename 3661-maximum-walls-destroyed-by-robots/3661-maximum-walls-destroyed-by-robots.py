from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # 1. Count walls exactly on robots (they are unconditionally destroyed)
        robot_set = set(robots)
        exact_walls = sum(1 for w in walls if w in robot_set)
        
        # 2. Filter out exact walls and sort the remaining for binary search
        filtered_walls = sorted([w for w in walls if w not in robot_set])
        
        def count_walls(a: int, b: int) -> int:
            """Helper to efficiently count walls strictly inside the inclusive range [a, b]."""
            if a > b:
                return 0
            # bisect_right finds the index strictly after 'b'
            # bisect_left finds the index of the first element >= 'a'
            return bisect_right(filtered_walls, b) - bisect_left(filtered_walls, a)
        
        # 3. Sort robots along with their bullet distances
        rob_dist = sorted(zip(robots, distance))
        n = len(rob_dist)
        
        # 4. DP Initialization for the very first robot
        R0, D0 = rob_dist[0]
        # Firing left destroys walls strictly before it
        prev_dp0 = count_walls(R0 - D0, R0 - 1) 
        # Firing right destroys 0 walls behind it
        prev_dp1 = 0                            
        
        # 5. DP Transitions for intermediate intervals
        for i in range(1, n):
            R_prev, D_prev = rob_dist[i-1]
            R_curr, D_curr = rob_dist[i]
            
            # Open interval boundaries strictly between adjacent robots
            L_bound = R_prev + 1
            R_bound = R_curr - 1
            
            if L_bound > R_bound:
                # No space between robots, so no walls can exist here
                c00 = c01 = c10 = c11 = 0
            else:
                # Calculate maximum bullet reach inside the current interval
                R_reach = min(R_bound, R_prev + D_prev)
                L_reach = max(L_bound, R_curr - D_curr)
                
                # Number of walls destroyed inside this interval based on firing choices
                c01 = 0 # Left robot fires Left, Right robot fires Right (Interval untouched)
                c11 = count_walls(L_bound, R_reach) if R_reach >= L_bound else 0 # Both fire Right
                c00 = count_walls(L_reach, R_bound) if L_reach <= R_bound else 0 # Both fire Left
                
                # Left robot fires Right, Right robot fires Left (Firing towards each other)
                if R_reach >= L_reach:
                    c10 = count_walls(L_bound, R_bound) # Paths overlap, entire inner span covered
                else:
                    c10 = c11 + c00 # Paths don't overlap, disjoint sum
                    
            # Update DP states based on the maximums from the previous robot
            curr_dp0 = max(prev_dp0 + c00, prev_dp1 + c10)
            curr_dp1 = max(prev_dp0 + c01, prev_dp1 + c11)
            
            prev_dp0, prev_dp1 = curr_dp0, curr_dp1
            
        # 6. Finalize the rightward boundary for the very last robot
        Rn_1, Dn_1 = rob_dist[-1]
        ans = max(prev_dp0, prev_dp1 + count_walls(Rn_1 + 1, Rn_1 + Dn_1))
        
        # Total walls = Walls on robots + Maximum walls destroyed in open intervals
        return exact_walls + ans