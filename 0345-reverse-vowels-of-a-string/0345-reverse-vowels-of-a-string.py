class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)
        #two pointer: scan from left and right
        left,right = 0, len(s)-1

        while left < right:
            while left < right and s_list[left] not in vowels:
                left +=1 #if not encountered vowels, keep going towards right
            while left < right and s_list[right] not in vowels:
                right -=1 #if not encountered vowels, keep going towards left

            s_list[left], s_list[right] = s_list[right], s_list[left] #when both on vowels, switch place

            #after switch, keep going
            left +=1
            right -=1
        
        return "".join(s_list)