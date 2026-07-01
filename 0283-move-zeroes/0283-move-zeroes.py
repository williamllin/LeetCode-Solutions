class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        
        #fast: scan from left to right
        for fast in range(len(nums)):
            #if the scanned number not 0
            if nums[fast] != 0:
                #switch place with slow
                nums[slow], nums[fast] = nums[fast], nums[slow]
                #move 1 to right, wait for the next !=0
                slow += 1