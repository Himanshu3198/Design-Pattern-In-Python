class Solution:

    def invalid(self,a,b) ->bool:
        if a == b:
            return True
        
        a_v = ord(a) -ord('a')
        b_v = ord(b) - ord('a')

        if abs(a_v-b_v) == 1:
            return True
        return False
        
    def removeAlmostEqualCharacters(self, word: str) -> int:

         x = '#'
         n = len(word)
         cnt = 0
         word = list(word)

         for i in range(0,n-1):            
            if self.invalid(word[i],word[i+1]):
                word[i+1] = x
                cnt += 1

         return cnt

            
        
