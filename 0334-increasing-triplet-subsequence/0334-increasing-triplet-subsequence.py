class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        '''
        first = float('inf')#first spot set as infinite number
        second = float('inf')

        #fill up three spots
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True #num is bigger than first and second->assign to third->True
        return False
        '''
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False