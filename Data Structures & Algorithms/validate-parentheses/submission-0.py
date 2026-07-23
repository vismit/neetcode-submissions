class Solution:
    def isValid(self, s: str) -> bool:
        seq = []
        map = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in s:
            if char in map:
                if seq and seq[-1] == map[char]:
                    seq.pop()
                else:
                    return False
            else:
                seq.append(char)
        return True if not seq else False
