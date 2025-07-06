
import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        """
        time = 1

        [enqueueTimei ,processingTimei  ]
        [,]
        time = 5 // while
        [4,1] // minheap check if the time matches [time + processing_time]
        minheap([6,1][5,2],[5,3])
        //time free, index == [0,2,3,1]

        time = 1

        [enqueueTimei ,processingTimei  ]

        time = 7 // mintime =
        [7,10, 0] // minheap check if the time matches [time + processing_time]
        minheap()
        //time free, index == [[9, 4],[11, 3],[12,2],[17,0][19, 1]]

        => [4,3,2,0,1]


        time =
        [[19,13,0],[16,9,1],[21,10,2],[32,25,3],[37,4,4],[49,24,5],[2,15, 6]]

        [[19,13,0],[16,9,1],[21,10,2],[32,25,3],[37,4,4],[49,24,5],]
        time = 3
        [2,15, 6] // minheap check if the time matches [time + processing_time]
        minheap()
        //time free, index == [[17,6]]

        => [4,3,2,0,1]
        """
        available_task_heap = []
        processing_task_heap = []
        res = []

        available_task_heap = [(e, p, i) for i, (e, p) in enumerate(tasks)]
        heapq.heapify(available_task_heap)
        # Initialize time to earliest enqueue
        if not available_task_heap:
            return []
        time = available_task_heap[0][0]
        # While tasks remain either to arrive or to process
        while available_task_heap or processing_task_heap:
            # Enqueue all tasks that have arrived by current time

            while available_task_heap and available_task_heap[0][0] <= time:
                e, p, idx = heapq.heappop(available_task_heap)
                # push by processingTime then idx
                heapq.heappush(processing_task_heap, (p, idx))

            if processing_task_heap:
                p, idx = heapq.heappop(processing_task_heap)
                res.append(idx)
                time += p

            else:
                time = available_task_heap[0][0]

        return res


if __name__ == '__main__':
    tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
    s = Solution()
    ans = s.getOrder(tasks)
    print(ans)