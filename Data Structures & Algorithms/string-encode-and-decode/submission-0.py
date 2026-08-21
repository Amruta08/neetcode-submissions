class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        # For every string compute length and append “length#string” to the result.
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
     
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # We use pointer i and j to track start and end of strings.
        while(i<len(s)):
            j=i
            while(s[j]!='#'):
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
