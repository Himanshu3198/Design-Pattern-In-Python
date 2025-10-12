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

    class Solution:
        def mergeAlternately(self, word1: str, word2: str) -> str:
            ans = []
            for w1, w2 in zip(word1, word2):
                ans.append(w1)
                ans.append(w2)
            ans.append(word1[len(word2):])
            ans.append(word2[len(word1):])
            return "".join(ans)

    class Solution:
        def is_alnum(self, s) -> bool:
            return s.isalnum()

        def isPalindrome(self, s: str) -> bool:

            i = 0
            j = len(s) - 1

            while i < j:

                if not self.is_alnum(s[i]):
                    i += 1
                    continue
                if not self.is_alnum(s[j]):
                    j -= 1
                    continue
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
            return True


