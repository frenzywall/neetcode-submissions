class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            # Format: Length + "#" + String Content
            encoded_string += str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        
        while i < len(s):
            j = i
            # Move j forward until we find the delimiter '#'
            while s[j] != "#":
                j += 1
            
            # The number between i and j is the length of the string
            length = int(s[i:j])
            
            # Start of the actual content is right after '#' (j + 1)
            # End of the content is start + length
            res.append(s[j + 1 : j + 1 + length])
            
            # Move our pointer i to the start of the next segment
            i = j + 1 + length
            
        return res