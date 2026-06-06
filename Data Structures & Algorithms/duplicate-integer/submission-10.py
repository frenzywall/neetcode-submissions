class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_set = []
        for i in nums:
            if i in seen_set:
                return True
            seen_set.append(i)
        return False
        