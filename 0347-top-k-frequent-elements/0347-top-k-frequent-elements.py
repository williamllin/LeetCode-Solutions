#import heapq
#from collections import Counter
#from typing import List


#當我們把元素丟進 Heap 時，如果 Heap 的大小超過了 $K$，就把此時「頻率最低」的頂端元素踢出去（heappop）。這樣一路走到最後，留在 Heap 裡面的，絕對就是全場最高頻的前 $K$ 個元素。
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Count the frequency of each number
        count = Counter(nums) #[1,1,1,2,2,3] -> {1: 3, 2: 2, 3: 1}
        
        #Maintain a Min-Heap of size K
        heap = []
        for num, freq in count.items():#items() so that get key and value
            #Python's heapq sorts by the first element of the tuple (freq)
            heapq.heappush(heap, (freq, num))

            # If heap size exceeds K, pop the element with the lowest frequency
            if len(heap) > k:
                heapq.heappop(heap)
        #Extract the numbers left in the heap (the top K frequent elements)      
        return [num for freq, num in heap]
        