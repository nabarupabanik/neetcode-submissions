class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset = {}
        for i in nums:
            hashset.setdefault(i, nums.count(i))

        l = []
        for _ in range(k):
            key = max(hashset, key=hashset.get)
            l.append(key)
            hashset.pop(key)

        return l

        
        
        