# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left<=right: #get a middle, gradually closing the boundaries
            mid = (left+right)//2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                right = mid-1
            elif res == 1:
                left = mid+1

        return -1 #make sure if number is not within 1 and n, still gets an int as ans
        