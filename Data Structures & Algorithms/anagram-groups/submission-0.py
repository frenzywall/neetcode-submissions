class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            c = tuple(sorted(word))
            if c not in seen:
                seen[c]=[word]
            else:
                seen[c].append(word)
        return list(seen.values())
        