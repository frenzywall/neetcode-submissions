class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest_streak = 1
        for num in nums:
            current_nums = num
            current_streak = 1
            while (current_nums + 1) in nums:
                current_nums += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)
        return longest_streak
        