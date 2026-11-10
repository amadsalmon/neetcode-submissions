from collections import Counter, deque
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        
        maxheap = []
        for task, freq in counter.items():
            maxheap.append((-1 * freq, task))
        heapify(maxheap)

        q = deque()

        cycles = 0

        while maxheap or q:
            while q and q[0][0] <= cycles:
                (_, freq, task) = q.popleft()
                heappush(maxheap, (freq, task))

            if maxheap:
                (freq, task) = heappop(maxheap)
                freq += 1

                if freq != 0:
                    q.append((cycles + n + 1, freq, task))

            cycles += 1

        return cycles

