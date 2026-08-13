class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        i,j = 0,0 #all start from the left of s,t string
        while i <len(s) and j <len(t):
            if s[i] == t[j]: 
                i+=1 #'only' if match, i move to next
            
            j+=1 #doesn't matter if match, j has to move on 
        
        return i == len(s)
        '''

        i,j=0,0 #start from left
        while i<len(s) and j<len(t):
            if s[i] == t[j]: #if match
                i+=1 #i move on
            j+=1 #j has to move always

        return i==len(s) #if i finished, True

