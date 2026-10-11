class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        arr = list(sorted(set(nums)))
        m = 1
        c = 1
        for i in range(len(arr)-1):
            if arr[i+1] == arr[i]+1:
                c += 1
            else:
                c, m = 1, max(c,m)
        return max(c,m)