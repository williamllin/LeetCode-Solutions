class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum = current_sum + nums[i] - nums[i-k] #plus next, and minus the first
            max_sum = max(max_sum, current_sum)
        return max_sum/k

        #1+12-5-6 = 2
        #range(4,6)
        #cs = 2 + nums[4] - nums[0] = 2+50-1 =51