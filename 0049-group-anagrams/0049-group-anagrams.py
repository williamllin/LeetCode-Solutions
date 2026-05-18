#from typing import List
#from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list) 
        #use this instead of {} so that when new key(aet) added will add new [] automatically
        

        for s in strs:
            sorted_s = "".join(sorted(s)) # "".join(['a','e','t']) -> aet
            anagram_map[sorted_s].append(s)
        return list(anagram_map.values())

        