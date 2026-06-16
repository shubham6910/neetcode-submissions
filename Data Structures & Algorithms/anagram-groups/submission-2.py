class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_map = defaultdict(list)
        # for st in strs: #O(n log k)
        #     key = ''.join(sorted(st))
        #     ans_map[key].append(st)
        # return list(ans_map.values())

        for st in strs:
            ch_list = [0]*26
            for c in st:
                ch_list[ord(c) - ord('a')] +=1
            key = tuple(ch_list)
            ans_map[key].append(st)
        return list(ans_map.values())