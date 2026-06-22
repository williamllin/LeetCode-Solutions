class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1: #if [str1str2] != [str2str1] then must be ""
            return ""

        #gcd: greatest common divisor
        gcd_length = math.gcd(len(str1), len(str2)) 
            #ex: ababab, abab/ math.gcd(6,4) = 2
        return str1[:gcd_length]
        