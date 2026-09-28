class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = [0]*26
        for c in s1:
            count[ord(c)-ord("a")]+=1

        window = [0]*26

        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1
            
        left=0
        right=len(s1)
        
        while right <= len(s2):
            
            # Current window is a permutation
            if window == count:
                return True

            # Remove character leaving the window
            window[ord(s2[left]) - ord('a')] -= 1

            # Add character entering the window
            if right < len(s2):
                window[ord(s2[right]) - ord('a')] += 1

            left += 1
            right += 1

        return False

