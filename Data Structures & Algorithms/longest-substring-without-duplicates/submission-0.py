class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # map that stores the last index where each character appeared
        mp = {}
        
        left = 0
        res = 0
        
        for right in range(len(s)):
            # When a character repeats, move the left pointer to one position after its previous occurrence
            if s[right] in mp:
                left = max(mp[s[right]]+1, left)
                
            # stores last index where character appeared
            mp[s[right]] = right
            
            # Calculate window size
            res = max(res, right-left+1)
        return res