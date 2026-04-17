class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_frequency = Counter(nums)
        items = count_frequency.items()
        sorted_items = sorted(items, key=lambda item:item[1], reverse=True)
        top_k = [item[0] for item in sorted_items[:k]]
        return top_k


            
        