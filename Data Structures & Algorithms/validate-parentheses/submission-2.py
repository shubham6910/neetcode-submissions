class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {')': '(', '}': '{', ']': '['}

        stk = []
        for c in s:
            if c not in par_dict:
                stk.append(c)
            else:
                if not stk: return False
                else:
                    popped = stk.pop()
                    # print(popped)
                    if popped != par_dict[c]:
                        return False
        return not stk