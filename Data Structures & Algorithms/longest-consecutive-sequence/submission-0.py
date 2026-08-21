class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        # for each num check if num-1 does not exist
        for num in numSet:
            if (num-1) not in numSet:
                # if num-1 doesn't exist, begin counting sequence
                length = 1
                while(num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest
        