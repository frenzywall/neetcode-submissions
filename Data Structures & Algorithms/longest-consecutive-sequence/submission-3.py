class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_set = set(nums)
        longest_streak = 0
        for n in sorted_set:
            if (n-1) not in sorted_set:
                current_num = n
                current_streak = 1
                while (current_num + 1) in sorted_set:
                    current_streak += 1
                    current_num +=1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak
        