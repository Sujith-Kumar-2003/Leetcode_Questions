from functools import lru_cache
from typing import List

class Solution:
    def beautifulNumbers(self, low: int, high: int) -> int:
        hehe = (low, high)

        def cnt(x: int) -> int:
            if x < 10:
                return x
            s = str(x)
            digs = []
            i = 0
            while i < len(s):
                digs.append(int(s[i]))
                i += 1
            n = len(digs)
            @lru_cache(maxsize=None)
            def dp(pos, tight, started, summ, prod):
                if pos == n:
                    if not started:
                        return 0
                    return 1 if (summ != 0 and prod % summ == 0) else 0
                lim = digs[pos] if tight else 9
                total = 0
                d = 0
                while d <= lim:
                    h = tight and (d == lim)
                    if not started:
                        if d == 0:
                            total += dp(pos + 1, h, False, 0, 1)
                        else:
                            total += dp(pos + 1, h, True, d, d)
                    else:
                        total += dp(pos + 1, h, True, summ + d, prod * d)
                    d += 1
                return total
            return dp(0, True, False, 0, 1)

        return cnt(high) - cnt(low - 1)
if __name__ == "__main__":
    sol = Solution()
    print(sol.beautifulNumbers(1, 1000000))
