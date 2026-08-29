class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap=[]
        for i in nums:
            if i not in hashmap:
                hashmap.append(i)
            else:
                return True
        return False