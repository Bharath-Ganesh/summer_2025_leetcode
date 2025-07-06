import heapq
from collections import Counter, defaultdict, deque
from typing import List


class Solution:
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #
    #     """
    #     ["A","A","A","B","B","B"], n = 2
    #     A - 4
    #     B - 3
    #     A, B, A, B, A, B, A
    #     """
    #
    #
    #
    #     lookUp = Counter(tasks)
    #     queue = deque()
    #     maxHeap = []
    #
    #     for task, freq in lookUp.items():
    #         heapq.heappush(maxHeap, (-1 * freq, task))
    #
    #     leastInterval = 0
    #     while maxHeap or queue:
    #         if maxHeap:
    #             _, task = heapq.heappop(maxHeap)
    #             lookUp[task] -= 1
    #             if lookUp[task] == 0:
    #                 del lookUp[task]
    #             else:
    #                 queue.append((leastInterval + 1 + n, task))
    #         else:
    #             if queue and queue[0][0] <= leastInterval:
    #                 _, task = queue.popleft()
    #                 heapq.heappush(maxHeap, (-1 * lookUp[task], task))
    #                 continue
    #         leastInterval += 1
    #     return leastInterval

    def leastInterval(self, tasks: List[str], n: int) -> int:

        """
        ["A","A","A","B","B","B"] , n = 2

        A - 3, B - 3, n = 2
                Time = 4 ((A,4))
        1 + 1 + 1 (idle_time) +
        heap  => [(A,2) (B,2)]
        queue => [(B,5)]
        """

        look_up_freq = Counter(tasks)
        max_heap = [(-val, key) for key, val in look_up_freq.items()]
        heapq.heapify(max_heap)

        queued_tasks = deque()
        time = 0

        while max_heap or queued_tasks:

            # task from cool down exist
            while queued_tasks and queued_tasks[0][0] <= time:
                _, task = queued_tasks.popleft()
                curr_freq = look_up_freq[task]
                heapq.heappush(max_heap, (-curr_freq, task))

            # task exist
            if max_heap:
                _, task = heapq.heappop(max_heap)
                look_up_freq[task] -= 1
                if look_up_freq[task]:
                    queued_tasks.append((time + n + 1, task))

            else:
                if queued_tasks:
                    queued_time, task = queued_tasks.popleft()
                    time+= (queued_time - time)
                    curr_freq = look_up_freq[task]
                    heapq.heappush(max_heap, (-curr_freq, task))
                    continue

            time += 1

        return time


if __name__ == '__main__':
    s = Solution()
    ans = s.leastInterval(["A","A","A","B","B","B"], n = 2)
    print(ans)