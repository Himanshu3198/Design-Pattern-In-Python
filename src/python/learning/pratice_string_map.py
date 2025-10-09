class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = defaultdict(list)

        for s in strs:
            t = ''.join(sorted(s))
            mp[t].append(s)

        result = list(mp.values())
        return result

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False;
        mp_s, mp_t = {}, {}
        for i in range(0, len(s)):

            if (s[i] in mp_s and mp_s[s[i]] != t[i]) or (t[i] in mp_t and mp_t[t[i]] != s[i]):
                return False;
            mp_s[s[i]] = t[i]
            mp_t[t[i]] = s[i]

        return True

    class Solution:
        def furthestDistanceFromOrigin(self, moves: str) -> int:
            mp = defaultdict(int)
            for s in moves:
                mp[s] += 1

            z = mp['_']
            l = mp['L']
            r = mp['R']

            ans = z + abs(l - r)

            return ans



