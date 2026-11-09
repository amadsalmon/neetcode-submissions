class Solution:
    """Various approaches below"""

    def majorityElement(self, nums: List[int]) -> int:
        #return self.majorityElement_counter(nums)
        #return self.majorityElement_sorting(nums)
        return self.majorityElement_fast(nums)

    def majorityElement_counter(self, nums: List[int]) -> int:
        """O(N) time and O(N) space"""
        counts = Counter(nums)
        majority_element, count = counts.most_common(1)[0]
        return majority_element

    def majorityElement_sorting(self, nums: List[int]) -> int:
        """
        O(N * log N) time and O(N) space because of sorting
        Relies on the fact that once sorted, the middle element is the majority element by definition. 
        """
        n = len(nums)
        mid = n // 2
        nums.sort()
        return nums[mid]

    def majorityElement_fast(self, nums: List[int]) -> int:
        """O(N) time and O(1) space"""
        current = None
        count = 0

        for n in nums:
            if count == 0:
                current = n
            count += 1 if n == current else -1
        return current
