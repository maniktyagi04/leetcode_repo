class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Count of odd and even numbers in each range
        o_n = (n + 1) // 2  # odd numbers in [1, n]
        e_n = n // 2        # even numbers in [1, n]
        o_m = (m + 1) // 2  # odd numbers in [1, m]
        e_m = m // 2        # even numbers in [1, m]

        # Odd sum pairs: odd+even or even+odd
        return o_n * e_m + e_n * o_m
