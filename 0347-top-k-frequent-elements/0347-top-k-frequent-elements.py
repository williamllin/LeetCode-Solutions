#import heapq
#from collections import Counter
#from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Count the frequency of each number
        count = Counter(nums) #[1,1,1,2,2,3] -> {1: 3, 2: 2, 3: 1}
        
        #Maintain a Min-Heap of size K
        heap = []
        for num, freq in count.items():
            #Python's heapq sorts by the first element of the tuple (freq)
            heapq.heappush(heap, (freq, num))

            # If heap size exceeds K, pop the element with the lowest frequency
            if len(heap) > k:
                heapq.heappop(heap)
        #Extract the numbers left in the heap (the top K frequent elements)      
        return [num for freq, num in heap]
        