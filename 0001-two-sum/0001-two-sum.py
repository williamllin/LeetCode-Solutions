class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        #Create a hash map to store value-to-index mappings: {value: index}
        for i, num in enumerate(nums): #get index(i) nad value(nums)
            complement = target - num #Calculate the required value needed to reach the target
            
            #if required value exist in map then return
            if complement in hashmap:
                #Return the index of the complement and the current index
                return [hashmap[complement], i]
            
            #Otherwise, store the current number and its index for future lookups
            hashmap[num] = i