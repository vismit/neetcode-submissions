class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        output = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] in res:
                l += 1
                res.pop(0)
            else:
                res.append(s[r])
                r += 1
            output = max(output, len(res))
        
        return output