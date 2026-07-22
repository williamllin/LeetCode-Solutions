class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, x in enumerate(nums): #enumerate: can get index(i) and element(x)
            if left_sum == total_sum - left_sum - x: #if left_sum == right_sum
                return i #return the 'index'

            left_sum += x
            
        return -1