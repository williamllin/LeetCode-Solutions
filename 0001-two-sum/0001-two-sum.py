class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        #Create a hash map to store value-to-index mappings: {value: index}
        for i, num in enumerate(nums): #Iterate through the list, getting both the index and the value
            complement = target - num #Calculate the required value needed to reach the target
            
            #If the complement exists in the map, a matching pair is found
            if complement in hashmap:
                #Return the index of the complement and the current index
                return [hashmap[complement], i]
            
            #Otherwise, store the current number and its index for future lookups
            hashmap[num] = i