class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""

        for ch in s.lower():
            if ch.isalnum():
                st += ch

        return st == st[::-1]
