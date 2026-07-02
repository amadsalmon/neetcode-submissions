class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def getAgeFromDetail(detail: str) -> int:
            return int(detail[11:13])
        
        count = 0
        
        for person in details:
            if getAgeFromDetail(person) > 60:
                count += 1
        
        return count