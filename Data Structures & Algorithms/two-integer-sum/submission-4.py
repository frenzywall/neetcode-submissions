class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            find = target - nums[i]
            if find in nums:
                j = nums.index(find)
                if i!=j:
                    return sorted([i,j])
        