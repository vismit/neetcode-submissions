class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for string in strs:
            found = False
            for key in temp.keys():
                if self.is_anagrams(string, key):
                    temp[key].append(string)
                    found = True
                    break
            if not found:
                temp[string].append(string)
        
        return list(temp.values())
                    

    def is_anagrams(self, str_1:str, str_2: str) -> bool:
        if len(str_1) != len(str_2):
            return False
        
        temp = dict()
        for i in range(len(str_1)):
            temp[str_1[i]] = 1 + temp.get(str_1[i], 0)
            temp[str_2[i]] = -1 + temp.get(str_2[i], 0)
        
        for key in temp.keys():
            if temp[key] != 0:
                return False
        return True