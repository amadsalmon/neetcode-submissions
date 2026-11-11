from heapq import heapify, heappush, heappop

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Initialize array with tuples (enqueueTimei, processingTimei, i) and sort it
        tasks_sorted = [(enqueueTimei, processingTimei, i) for i, [enqueueTimei, processingTimei] in enumerate(tasks)]
        tasks_sorted.sort()

        print(f"tasks_sorted: {tasks_sorted}")

        ready_tasks = []  # Min-heap

        task_order = []
        clock = 1
        t = 0
        
        # Loop through all tasks
        while t < len(tasks) or ready_tasks:
            # Check if tasks are ready to be enqueued (enqueue time <= current clock)
            # Put all the ready tasks in the heap (but remove enqueue time from the tuple, doesn't matter anymore)
            # If heap is empty: move pointer n on array by one position
            if not ready_tasks:
                clock = max(clock, tasks_sorted[t][0])
                
            while t < len(tasks) and tasks_sorted[t][0] <= clock:
                _, task_processingTime, task_i = tasks_sorted[t]
                heappush(ready_tasks, (task_processingTime, task_i))
                t += 1
            

            # Pop the heap
            # Add index of popped task to task_order 
            # Advance clock by the processing time of the popped task
            task_processingTime, task_i = heappop(ready_tasks)
            clock += task_processingTime
            task_order.append(task_i)

        return task_order
        