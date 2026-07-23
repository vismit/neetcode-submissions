class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(char for char in s if char.isalnum()).lower()
        for index in range(int(len(string) / 2)):
            if string[index] != string[len(string) - index - 1]:
                return False
        return True