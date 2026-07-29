class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = []

        for spell in spells:
            min_potion_required = (success + spell - 1)//spell #spell*potion>=success, potion>=success//spell
            #7//5=1, but we need at least 2, so use integer arithmetic((7+5-1)//5=2)

            #Binary search for the first potion >= min_potion
            left, right = 0, m - 1
            idx = m #Default to m if no potion satisfies the condition
            
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= min_potion_required:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            #All potions from 'idx' to the end are valid
            ans.append(m - idx)
            
        return ans