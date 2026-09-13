class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) >> 1 #same as // this >> bitwise op also divides by 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left
