class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Find the index where target should be inserted in a sorted array.
        If target exists, return its index. Otherwise, return the insertion position.

        Args:
            nums: A sorted array of integers in ascending order
            target: The target value to search for or insert

        Returns:
            The index where target is found or should be inserted
        """
        # Initialize binary search boundaries
        # left points to the start, right points one past the end (exclusive)
        left, right = 0, len(nums)

        # Binary search to find the leftmost position where nums[i] >= target
        while left < right:
            # Calculate middle index using bit shift (equivalent to // 2)
            mid = (left + right) >> 1

            # If middle element is greater than or equal to target,
            # the answer is in the left half (including mid)
            if nums[mid] >= target:
                right = mid
            else:
                # Otherwise, the answer is in the right half (excluding mid)
                left = mid + 1

        # left now points to the first position where nums[i] >= target
        # or to len(nums) if all elements are smaller than target
        return left
