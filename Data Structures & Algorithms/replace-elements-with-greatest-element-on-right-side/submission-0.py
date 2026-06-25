class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largestElement = arr[-1]
        for i in range(1,len(arr)):
            print(f"inspecting element position {len(arr)-i} (val {arr[len(arr)-i]}).")
            current = arr[len(arr)-i]
            arr[len(arr)-i] = largestElement
            
            if current > largestElement:
                largestElement = current
                print(f"  New  largestElement = {largestElement} - element position {len(arr)-i} (val {current}).")
        
        arr[0]= largestElement
        arr[-1] = -1

        return arr
