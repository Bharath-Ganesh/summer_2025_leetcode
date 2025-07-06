import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """
        [enque, index, processing]
        arr = [[2,1,4],[3,2,2],[4,3,1]] # sorted by enque time
        Time = 1
        arr = [[2,1,0],[4,1,2],[2,2,3],[1,3,4]]
        processing_time, index, enque
        time = 1 +2 = 3
        heap : [[4,1,2],[2,33,2,2]]

        0,
        """
        arr = [(enqueTime, idx, processingTime) for idx, (enqueTime, processingTime ) in enumerate(tasks)]
        arr.sort(key=lambda x: x[0])
        time = 1
        idx = 0
        minheap = []
        res = []
        while idx < len(arr) or minheap:
            # enque time
            while idx < len(arr) and arr[idx][0] <= time:
                _, task_no, processingTime = arr[idx]
                heapq.heappush(minheap, (processingTime, idx))
                idx += 1

            if minheap:
                processingTime, completed_task_no = heapq.heappop(minheap)
                time += processingTime
                res.append(completed_task_no)
                continue
            else:
                # no task assigned
                if idx + 1 < len(arr):
                    time = arr[idx + 1][0]
                    continue
            time += 1

        return res

if __name__ == '__main__':
    s = Solution()
    ans = s.getOrder([[7,10],[7,12],[7,5],[7,4],[7,2]])
    print(ans)