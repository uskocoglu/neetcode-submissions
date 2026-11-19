class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenVals = {}
        for num in nums:
            if seenVals.get(num) != None:
                return True
            seenVals[num] = "val"
        return False
        