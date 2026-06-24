class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)

        for i in range(length): #if spot planted, move on
            if flowerbed[i]==1:
                continue

            left_empty = (i==0) or (flowerbed[i-1]==0) #left to the spot empty
            right_empty = (i == length-1) or (flowerbed[i+1]==0) #right to the spot empty

            if left_empty and right_empty: #both sides empty -> plant a flower and -1 flower in hand
                flowerbed[i]=1
                n-=1

                if n<=0: #for performance optimization: if no flower, no need to scan the rest spots
                    return True
        return n<=0


        