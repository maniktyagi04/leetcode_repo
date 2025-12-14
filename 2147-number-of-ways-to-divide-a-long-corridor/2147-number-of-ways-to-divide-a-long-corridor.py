class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        total_seats = corridor.count('S')
        if total_seats == 0 or total_seats % 2 == 1:
            return 0

        ways = 1
        seat_count = 0
        plant_count = 0
        started = False  # indicates first section is formed

        for ch in corridor:
            if ch == 'S':
                seat_count += 1
                if seat_count == 2:
                    if started:
                        ways = (ways * (plant_count + 1)) % MOD
                    started = True
                    seat_count = 0
                    plant_count = 0
            else:  # 'P'
                if started and seat_count == 0:
                    plant_count += 1

        return ways

        