class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_map = defaultdict(list)

        for st in strs:
            key = ''.join(sorted(st))
            ans_map[key].append(st)
        return list(ans_map.values())