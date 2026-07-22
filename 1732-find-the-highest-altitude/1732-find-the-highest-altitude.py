class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_alt = 0
        max_alt = 0

        for i in range(len(gain)):
            current_alt = current_alt + int(gain[i])
            max_alt = max(max_alt, current_alt)
        return max_alt