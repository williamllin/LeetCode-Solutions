#import heapq
#from collections import Counter
#from typing import List


#heap堆積: 只保證最頂端是極值，不保證整組資料是排序好的


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Step 1: Count the frequency of each number
        #Ex: [1,1,1,2,2,3] -> {1: 3, 2: 2, 3: 1}
        count = Counter(nums)

        #Step 2: Initialize an empty list to serve as our Min-Heap
        heap =[]

        #Step 3: Iterate through unique numbers and their frequencies
        for num, freq in count.items():

            heapq.heappush(heap,(freq,num))#Push (freq, num) tuple into the heap, heapq:smallest on top, if want biggest: -num

            if len(heap)>k:#Keep heap size <= k by removing the element with the smallest frequency
                heapq.heappop(heap)

        #Step 4: Extract and return the numbers from the top k elements left in the heap
        return [num for freq, num in heap]        











