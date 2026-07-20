class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #delete one '0' -> find longest 1s with one '0', and then minus 1
        #Question 1004 but as k=1
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1
            
            while zero_count > 1:
                if nums[left]==0:
                    zero_count-=1
                left+=1
            
            max_len = max(max_len, right-left+1)
        return max_len -1
