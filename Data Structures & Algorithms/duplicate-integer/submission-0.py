class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result_set = set()
        for n in nums:
            freq = 0
            if n in result_set:
                return True
            else: 
                result_set.add(n)
        return False
        