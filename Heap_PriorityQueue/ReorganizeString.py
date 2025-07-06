import heapq
from collections import deque, Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
            aaab
            a:3, b:1

            aab
            a:1, b:1
            ab
        """
        lookup = Counter(s)
        maxheap = [ (-cnt, key) for key, cnt in lookup.items()]
        heapq.heapify(maxheap)
        res = []
        while maxheap:
            cnt, key = heapq.heappop(maxheap)
            if len(res) > 0 and res[-1] == key:
                if not maxheap:
                    return ""
                second_cnt, second_key = heapq.heappop(maxheap)
                res.append(second_key)
                second_cnt += 1
                if second_cnt:
                    heapq.heappush(maxheap, (second_cnt, second_key))
            else:
                res.append(key)
                cnt += 1
            if cnt:
                heapq.heappush(maxheap, (cnt, key))

        return "".join(res) if len(res) == len(s) else ""



if __name__ == '__main__':
    sol = Solution()
    print(sol.reorganizeString("baaba"))