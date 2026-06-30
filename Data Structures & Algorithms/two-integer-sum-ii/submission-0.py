class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        n = len(numbers)
        for i in range(0, n-1):
            for j in range(i+1, n):
                if numbers[i]+numbers[j] == target:
                    return [i+1,j+1]
        return [0,0]