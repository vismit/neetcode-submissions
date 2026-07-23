class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0 

        for number in nums:
            if number:
                total_product *= number
            else:
                zero_count += 1
        
        if zero_count > 1: return [0] * len(nums)

        result = [0] * len(nums)
        for index, number in enumerate(nums):
            if zero_count: result[index] = 0 if number else total_product
            else: result[index] = total_product // number

        return result
        