class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_frequency = Counter(nums)
        reps = []
        for item in range(k):
            max_key = max(count_frequency,key=count_frequency.get)
            reps.append(max_key)
            del count_frequency[max_key]
        return reps
                
            
        