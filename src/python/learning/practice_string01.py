class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        n = len(strs[0])
        ans = ""

        for i in range(0, n):
            c = strs[0][i]

            for j in range(1, len(strs)):
                if i >= len(strs[j]) or c != strs[j][i]:
                    return ans
            ans += c

        return ans

