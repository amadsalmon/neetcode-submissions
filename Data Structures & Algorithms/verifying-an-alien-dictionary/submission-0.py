class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def buildOrder(order: str) -> dict[str: int]:
            res = {}
            for i, l in enumerate(order):
                res[l] = i
            return res
        
        def areLexicographicallyOrdered(a: str, b: str, lexicalorder: dict[str: int]) -> bool:
            for i in range(min(len(a), len(b))):
                if lexicalorder[a[i]] < lexicalorder[b[i]]:
                    return True
                if lexicalorder[a[i]] > lexicalorder[b[i]]:
                    return False
            if len(a) > len(b): 
                return False
            return True
            
        alien_order = buildOrder(order)

        # Compare words two by two
        for i in range(1, len(words)):
            if not areLexicographicallyOrdered(words[i-1], words[i], alien_order):
                return False

        return True
