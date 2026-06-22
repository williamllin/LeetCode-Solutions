class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #Two-Pointer
        result = []
        i, j = 0, 0 #two pointers, pointing at the start of word1 and word2

        #ex: word1="ab", word2="pqrs"
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1

        #(following the top codes)if one still have words left, stick the rest with no space
        #ex: word1 is done, word2 still have "rs" -> append(word2[j:])
        if i < len(word1):
            result.append(word1[i:])
        if j < len(word2):
            result.append(word2[j:])
        return "".join(result)

   

        