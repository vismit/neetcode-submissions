class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        output = 0
        seq = defaultdict(int)

        for number in nums:
            if not seq[number]:
                seq[number] = seq[number - 1] + seq[number + 1] + 1
                seq[number - seq[number - 1]] = seq[number]
                seq[number + seq[number + 1]] = seq[number]
                output = max(output, seq[number])
        
        return output