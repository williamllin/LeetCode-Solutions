class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        #binary search for local peak -> O(log n)
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            
            #compare mid element with its right neighbor
            if nums[mid] < nums[mid + 1]:
                left = mid + 1 #incline, peak on the right
            else:
                right = mid #decline, peak is mid or to the left

        #when left == right, we have converged on a peak index
        return left


#nums[-1]=nums[n]=-∞, meaning there must be a peak on either side, 