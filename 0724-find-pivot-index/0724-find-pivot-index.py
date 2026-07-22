class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        

        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == total_sum -left_sum -nums[i]:
                return i
            left_sum+=nums[i]
        return -1
'''
index(0) 0 == 28 -0 -1 =27(X)
index(1) 1 == 28 -1 -7 =20(X)
index(2) 8 == 28 -8 -3 =17(X)
index(3) 11 == 28 -11 -6 =11(O)

        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i

            left_sum += nums[i]

        return -1
        '''