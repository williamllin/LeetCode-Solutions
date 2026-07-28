from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        #operation1: the appearence of each char must be the same ([abc] [abs](X))
        if set(c1.keys()) != set(c2.keys()):
            return False

        #operation2: the 'set of number' 'of occurence' must be the same ([a2c3b4] [c2b3a4](O))
        return sorted(c1.values()) == sorted(c2.values())
