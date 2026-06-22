class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #Two-Pointer
        result = []
        i, j = 0, 0 #two pointers, pointing at the start of word1 and word2

        #if both still have words, take turns
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1
        #if one side is longer, the rest pack together
        if i < len(word1):
            result.append(word1[i:])
        if j < len(word2):
            result.append(word2[j:])
        return "".join(result)


        