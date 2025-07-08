class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)

        max_len = 0

        for n in num_set:
            if (n-1) not in num_set:
                current_start = n
                current_len = 1

                while (current_start + 1) in num_set:
                    current_start += 1
                    current_len += 1
                
                max_len = max(current_len, max_len)
            
        return max_len
        
