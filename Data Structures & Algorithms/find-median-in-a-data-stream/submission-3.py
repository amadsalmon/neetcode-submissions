from heapq import heapify, heappop, heappush


class MedianFinder:
    def __init__(self): 
        self.left = []  # this will be a max-heap
        self.right = []  # this will be a min-heap -> this is the one we prioritize
    
    def addNum(self, num: num) -> None:
        if not self.right:  # only need to check the right one to know if the stream is empty
            heapq.heappush(self.right, num)
        
        elif num >= self.right[0]:
            heapq.heappush(self.right, num)
            
            # Re-equilibrate if needed
            if len(self.left) + 1 < len(self.right):
                popped = -1 * heapq.heappop(self.right)
                heapq.heappush(self.left, popped)
        
        else:
            heapq.heappush(self.left, -1 * num)
            
            # Re-equilibrate if needed
            if len(self.left) > len(self.right):
                popped = -1 * heapq.heappop(self.left)
                heapq.heappush(self.right, popped)
            
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-1 * self.left[0] + self.right[0]) / 2
        else:
            return self.right[0]


"""
REASONING BELOW

[1, 2, 3] -> median is 2
    |

[1, 2, 3, 4, 5, 6, 7] -> 4
          |

[1,2,3,4] -> even length. (2+3)/2 = 2.5
    |


Question: is the median always the middle of a a list of integers, even if the integers are not consecutive?
  E.g. [1,5,100] -> by the definition of the problem the median would be 5, but that's not the real median??

The MedianFinder needs to work on a stream, not a given fixed array.  
First thought: we need to use two min heaps for this. 
The goal is to always have the two streams at the same length +- 1 
(e.g. one heap of length n, one of n+1 for uneven lengths)
The head of one of the two heaps would be the median.

For that we'd need to use one max-heap and one min-heap, because we'd like them to store:


 max-heap       min-heap
[1, 2, 3] and [4, 5, 6, 7]  -> median is 4
       |       | 
      head    head
 
Because it's a stream, we have to keep the heaps balanced in length (+-1) and reequilibrate according to the new elements coming.

E.g.: Consider we already have the two heaps above.
  - We want to "addNum(8)". 
  - We need to decide in which heap the 8 goes, we do that by checking both heaps' heads:
    - If element is <= max-heap[0]: needs to go into max-heap. 
    - If element is >= min-heap[0]: needs to go into min-heap.  (the case for 8 in our example)

    Heaps become: 

    max-heap       min-heap 
    [1, 2, 3] and [4, 5, 6, 7, 8]  
           |       | 
        head    head

    But how to keep the heaps balanced? We need to have a balance mechanism. E.g. after inserting an     
    element in one of the heaps, we check the lengths of the two and we pop the largest heap until the 
    heaps' lengths equalize (with a tolerance of 1 length of difference)


    Heaps become: 

    max-heap       min-heap
    [1, 2, 3, 4] and [5, 6, 7, 8] 
              |       | 
             head    head

    And findMedian becomes: if total len is even, median=(maxheap[0]+minheap[0])/2, otherwise simply minheap[0].

    Now we need to handle the example where the integers are not consecutive, but the problem definition isn't clear about that. I'd clarify with the interviewer.
"""