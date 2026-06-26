class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
        #s.split() -> make split using all kinds of spaces
        #[::1] -> reverse
        #" ".join -> stick back by single space