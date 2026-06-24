class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        
        for i in range(length):
            #if already planted, skip it
            if flowerbed[i] == 1:
                continue
                
            #spot that is empty at left([0] and [i-1] is '0')
            left_empty = (i == 0) or (flowerbed[i - 1] == 0)
            
            #spot that is empty at right([last one] and [i+1] is '0')
            right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
            
            #if left and right both empty
            if left_empty and right_empty:
                flowerbed[i] = 1  #plant one flower 0->1
                n -= 1            #one less flower on hand
                
                #if no flower then done, so no need to scan through the rest spots
                if n <= 0:
                    return True
                    
        #if planted all then True, else  false
        return n <= 0