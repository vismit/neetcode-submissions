class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            count = [0] * 26 # a-z

            for char in string:
                count[ord(char) - ord("a")] += 1

                # a -> 0 = 80 - 80
                # c -> 2 = 82 - 80

            result[tuple(count)].append(string)

        return list(result.values())