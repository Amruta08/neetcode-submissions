class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # return "" if string t is empty
        if t == "":
            return ""
     
        countT, window = {}, {}
        # Build frequency map for characters in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
     
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        left = 0
     
        for right in range(len(s)):
            # track frequency of each character in window
            c = s[right]
            window[c] = 1 + window.get(c, 0)
            
            # Check if window is valid, but checking all character frequencies 
            if c in countT and window[c] == countT[c]:
                have += 1
         
            while have == need:
                # Update result
                if (right-left+1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                # Shrink window by moving left pointer ahead
                window[s[left]] -= 1
                # Check if the shrunk window is valid
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
                
        # return result
        left, right = res
        return s[left:right+1] if resLen != float("infinity") else ""