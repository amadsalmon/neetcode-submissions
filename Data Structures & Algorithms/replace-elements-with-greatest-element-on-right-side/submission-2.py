class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largestElement = arr[-1]
        for i in range(1,len(arr)+1):
            current = arr[len(arr)-i]
            arr[len(arr)-i] = largestElement
            
            if current > largestElement:
                largestElement = current
        
        arr[-1] = -1

        return arr
