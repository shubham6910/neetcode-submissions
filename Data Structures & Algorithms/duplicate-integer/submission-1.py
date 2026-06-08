class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result_set = set()
        for n in nums:
            if n in result_set:
                return True
            else: 
                result_set.add(n)
        return False
        