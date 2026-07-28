from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        return len(counts.values()) == len(set(counts.values()))#number of occurs, if == distinct occurs

        '''
        [1,2,2,1,1,3]
        len(counts.values()) =3 len('1'->3/ '2'->2/ '3'->1)
        len(set(counts.values())) =3 len(3,2,1)

        [1,2]
        len(counts.values()) =2 len('1'->1, '2'->1)
        len(set(counts.values())) =1 len(1)
        '''
