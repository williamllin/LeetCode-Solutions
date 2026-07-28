from collections import Counter
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)
        #list is mutable so can't use as key of dictionary or counter
        #tuple is immutable and can use as key of hash table
        row_counts = Counter(tuple(row) for row in grid)

        ans = 0

        #take out each column and compare
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            ans += row_counts[col] #if col in row_counts, add 

        return ans