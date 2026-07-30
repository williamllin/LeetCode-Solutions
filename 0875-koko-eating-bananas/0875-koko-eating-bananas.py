class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        #minimum speed 'k' to finish all bananas in 'h' hours
        #range of k: (1,max(piles))
        left, right = 1, max(piles)
        while left < right:
            mid = (left+right)//2

            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours <=h:
                right = mid
            else: 
                left = mid+1
        
        return left
'''      
piles = [30,11,23,4,20], h = 5

ROUND1:
mid=(1+30)//2 = 15
pile1 -> 30/15 =2hr
...
pile5 -> 20/15 =2hr
total: 8hrs (>h, so left = mid+1)

ROUND2:
mid=(16+30)//2 = 23
pile1 -> 30/23 =2hr
...
pile5 -> 20/23 =1hr
total: 6hrs (>h, so left = mid+1)

ROUND3:
...
...

ROUND4(left = 28)
mid=(28+30)//2 = 29 
...
total: 6hrs

ROUND5(left = 30)
while left<right (X)
return 30
'''