class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        temp = dict()
        for i in range(len(s)):
            temp[s[i]] = 1 + temp.get(s[i], 0)
            temp[t[i]] = -1 + temp.get(t[i], 0)

        for key in temp.keys():
            if temp[key] != 0:
                return False
        return True