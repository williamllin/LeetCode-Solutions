class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        current_vowels = 0

        #count the vowels in first window(first kth chars)
        for i in range(k):
            if s[i] in vowels:
                current_vowels+=1

        max_vowels = current_vowels
        if max_vowels == k:#if already max out then stop

            return k

        
        #sliding window
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            #to see if the old head is a vowel
            if s[i - k] in vowels:
                current_vowels -= 1

            max_vowels = max(max_vowels, current_vowels)
            if max_vowels == k:
                return k

        return max_vowels

#ex:abciiidef
#first window: s[0:3] = 'abc', current_vowels =1, max_vowels =1

# first sliding window: i=3 = 'i', (s[3] is i so +1, s[3-3] is a so -1), cv =1+1-1 =1
#second sliding window: i=4 = 'i', (s[4] is i so +1, s[4-3] is b so +0), cv =1+1+0 =2
# third sliding window: i=5 = 'i', (s[5] is i so +1, s[5-3] is c sp +0), cv =2+1+0 =3
#max_vowels = k -> stop and return k