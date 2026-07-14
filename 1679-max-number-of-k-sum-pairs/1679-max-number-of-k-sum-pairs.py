class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort() #sort the list first
        operation = 0
        left = 0
        right = len(nums)-1

        while left<right:
            current_sum = nums[left]+nums[right]
            if current_sum == k: #if equal k, both move inside
                left+=1
                right-=1
                operation+=1
            elif current_sum<k: #if smaller, increase the sum
                left+=1
            else:
                right-=1 #if bigger, decrease the sum
                
        return operation
