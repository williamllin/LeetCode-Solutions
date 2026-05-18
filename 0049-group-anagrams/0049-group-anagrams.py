#from typing import List
#from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) #use this instead of {} so that when new key(aet) added will add new [] automatically
        
        for s in strs:
            #Sort the characters of the string and join them back into a string
            sorted_s = "".join(sorted(s)) 
            anagram_map[sorted_s].append(s)
        return list(anagram_map.values())

        