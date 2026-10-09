import array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # In case the n is lesser
        # def traverse(i, prev):
        #     if i >= len(nums):
        #         return 1
        #     curr = nums[i]
        #     fut = traverse(i+1, prev * curr)
        #     nums[i] = prev * fut
        #     return curr * fut
        prev = 1
        result = array.array("i", [1]*len(nums))
        for i in range(len(nums)):
            result[i] = prev
            prev *= nums[i]

        fut = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= fut
            fut *= nums[i] 
        return list(result)