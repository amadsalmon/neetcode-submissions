class Solution:

    """
    # Ideas

    _(Simplifying below: L = M + N)_

    ## Brute force

    First brute force solution would be to simply combine the two arrays into 
    one, sort that combined array, and take the median by finding the element 
    in the middle of it.
    That would be O(L.log(L)) because of the sorting.

    ## Slightly less brute, slightly more optimized:

    We can adopt the same approach as the previous solution, but this time 
    taking advantage of the two arrays being already sorted, as such 
    reconstructing the total sorted array element by element.
    That would be O(L).

    ## Can we do even better?

    Better than O(L) would be O(log L). Mmm, that makes me think of binary search.
    I'm not sure how to incorporate binary search into this problem though.
    The O(log L) complexity already discards the option of combining the arrays, 
    (as that operation would be O(L)). So we need a solution where we keep both 
    arrays in place. Maybe we need to operate on both of them at the same time.
    Seems like there is something to do with having two pointers on both arrays 
    at the same time indeed.
    Thinking...

    Binary search is good for specifically finding an element in an array fast, 
    but here our element is not a fixed value, rather it depends on its position 
    in the total list of all values. 
    So perhaps we need to reason with indices because the index of the median in 
    the total array is the only thing we know for sure.
    If we have arrays of length M and N, the median will, always, be at index (M + N) // 2. 
    Maybe we can start by understanding where that index would fall.
    
    First I notice a clear special case: if the two arrays don't have overlap: 
    [1,2,3] [100] -> median is 3, 
    no need for complex logic. We'd just check the extremities of both arrays to 
    determine if there's overlap (if (nums1[-1] <= nums2[0]) or (nums2[-1] <= nums1[0])).
    In such case the index would be computed as before, and we'd find it easily.

    That leaves us (back) to the other case where there IS overlap between the two arrays.
    How to determine the index of such an element?

    Maybe I'm wrong going with indices. Maybe I should think more about the values themselves...

    So if we perform a binary search spanning both arrays at once.
    We first need to understand in which kind of overlap we are.

    A) Complete occlusion: one array's value are completely inside the other's bound: 
    nums1[0] <= nums2[0] and nums2[-1] <= nums1[-1]
    [.......nums1.........] 
         [...nums2....]

    B) Partial overlap: 
    nums1[0] <= nums2[0] and nums2[-1] > nums1[-1]
    [.....nums1.......]
           [.....nums2.......]
        

    So depending on that we could perform our search? I'm not going anywhere I feel...
    And this splitting arrays is just going to make the code a mess.

    OK we could do something, going back to the index of the median.
    The independant medians of the two single arrays dont help us find the global median.
    So what if we tried to recreate the total array without actually recreating it?
    That would require us to kind of find the point in both arrays where the global median is.
    What would that look like?
    That would require us to find TWO points i,j that cut nums1 and num2 in two 
    while satisfying a rule: all elements before i o j are smaller than the elements after i and j.
    But how does that ensure that this split cuts the global array in half?

    L//2. So the global median is at half. 
    So if we pick an index i, necessarily j will have to be  L//2 - i.

    Here we go.
    This is what we need the binary search for.

    At each turn: pick i according to a binary search algorithm, and j = L//2 - i.

    We split the arrays at i and j, and check that the left halves contain 
    elements all smaller than the right half:
    - nums1[i] <= nums2[j+1] and nums2[j] <= nums1[i+1] (C)

    If those conditions are not true, we need to increase or decrease i through 
    the binary search algorithm to ensure we find a half satisfying condition (C) above.
    """


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        half = (n + m) //2
        
        # If there is overlap, do binary search O(log(m+n))
        if n > m:
            # Ensure nums1 is the smallest array for simplicity
            return self.findMedianSortedArrays(nums2, nums1)

        l, r = 0, n
        while l <= r:
            i = (l + r) // 2
            j = half - i

            A_right = nums1[i] if i < n else float('inf')
            A_left  = nums1[i-1] if i > 0 else float('-inf') 
            B_right = nums2[j] if j < m else float('inf')
            B_left  = nums2[j-1] if j > 0 else float('-inf') 

            if A_left <= B_right and B_left <= A_right:
                # Good! We split the halves in a satisfying way, we stop
                if (n + m) % 2 == 0:
                    left_max = max(A_left, B_left)
                    right_min = min(A_right, B_right)
                    return (left_max + right_min) / 2
                else:
                    return min(A_right, B_right)
            elif A_left > B_right:
                r = i - 1
            elif B_left > A_right:
                l = i + 1

        return -1






        