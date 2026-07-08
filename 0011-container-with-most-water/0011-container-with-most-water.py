class Solution:
    def maxArea(self, height: List[int]) -> int:
        #初始化雙指標，站在最兩端（此時底最大）
        left = 0
        right = len(height) - 1
        max_water = 0  #用來記錄當前最大面積
        
        #指標還沒相遇時
        while left < right:
            width = right - left #底
            current_height = min(height[left], height[right]) #高(較矮的那根)
            current_water = width * current_height #面積
            
            #與當前最大面積比
            max_water = max(max_water, current_water)
            
            #矮的那根繼續往內走，看可不可以遇到更高柱子
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
