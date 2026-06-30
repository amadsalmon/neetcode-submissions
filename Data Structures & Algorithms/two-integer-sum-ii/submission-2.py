class Solution:
    """
    Better O(N) solution taking advantage of the fact that the array is sorted
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1 

        while left < right:
            current = numbers[left] + numbers[right]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                return [left + 1 , right + 1]

        return [0, 0]

    """
    Brute force O(N^2) solution
    """
    def twoSum_v0(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(0, n-1):
            for j in range(i+1, n):
                if numbers[i]+numbers[j] == target:
                    return [i+1,j+1]
        return [0,0]