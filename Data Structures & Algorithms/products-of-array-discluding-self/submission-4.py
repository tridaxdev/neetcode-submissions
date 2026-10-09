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
        p = 1
        r = [0] * len(nums)
        for i in range(len(nums)):
            r[i] = p
            p *= nums[i]

        f = 1
        for i in range(len(nums)-1, -1, -1):
            r[i] *= f
            f *= nums[i] 
        return r