from itertools import permutations
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        total = 0
        seen = set()
        for perm in permutations(sorted(digits), 3):
            if perm[0] == 0:
                continue
            if perm[2] == 0:
                continue
            if perm[2] % 2 != 0:
                continue
            if perm not in seen:
                seen.add(perm)
                total += 1
        return total

if __name__ == "__main__":
    sol = Solution()
    print(sol.totalNumbers([1, 2, 3, 4]))
