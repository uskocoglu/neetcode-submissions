class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre, post = 1, 1
        for num in nums:
            res.append(pre)
            pre = num * pre
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * post
            post = post * nums[i]
        
        return res