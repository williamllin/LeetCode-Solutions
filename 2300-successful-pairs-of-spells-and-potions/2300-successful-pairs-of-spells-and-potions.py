class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = []

        for spell in spells:
            min_potion_required = (success + spell - 1) // spell
            left, right = 0, m - 1
            idx = m  # 預設為 m，代表如果都沒找到，符合數就是 m - m = 0
            
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] >= min_potion_required:
                    idx = mid         # 找到了，但繼續往左邊找「更靠左」的第一個符合位置
                    right = mid - 1
                else:
                    left = mid + 1
            
            # 成功數量 = 總長度 - 第一個符合條件的 Index
            ans.append(m - idx)
            
        return ans