class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        result = [[] for i in range(len(nums) + 1)]

        for number in nums:
            count[number] = 1 + count.get(number, 0)

        for key, count in count.items():
            result[count].append(key)

        output = []

        for i in range(len(result) - 1, 0, -1):
            for n in result[i]:
                output.append(n)
                if len(output) == k:
                    return output