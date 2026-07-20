class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zero_count = 0
        max_len = 0
        #for loop default 'right' as 0
        for right in range(len(nums)): #right pointer moving towards right
            if nums[right]==0: #if new tail is 0, zero count add 1
                zero_count+=1

            while zero_count > k: #if exceed k, left pointer starts moving right, and if new left is 0, count minus 1
                if nums[left]==0:
                    zero_count-=1
                left+=1

            max_len = max(max_len, right-left+1)

        return max_len 