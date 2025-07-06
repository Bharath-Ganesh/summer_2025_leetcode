import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
            a = 8, b = 0, c = 11
            c - 3, a - 2
            ccaaccaaccaaccaacc
            ccaccaccaaccaaccaac
            c - 8 a - 6

            maxheap [("c", 7),("b", 1),("a", 1)]

            maxheap [("a", 1)]
            b = 1
            temp = ["c", "c", "b" ]

            """
        maxheap= []
        for key, val in {"a": a, "b": b, "c": c}.items():
            if val > 0:
                maxheap.append((-val, key))
        heapq.heapify(maxheap)

        res = []
        while maxheap:
            first_val, first_key = heapq.heappop(maxheap)
            # Three occurence of the same characters
            if len(res) > 1 and res[-1] == res[-2] and res[-1] == first_key:
                if not maxheap:
                    return "".join(res)
                second_val, second_key = heapq.heappop(maxheap)
                res.append(second_key)
                second_val += 1
                if second_val:
                    heapq.heappush(maxheap, (second_val, second_key))
            else:
                res.append(first_key)
                first_val += 1
            if first_val:
                heapq.heappush(maxheap, (first_val, first_key))

        return "".join(res)

if __name__ == "__main__":
    s = Solution()
    ans = s.longestDiverseString(a = 7, b = 1, c = 0)
    print(ans)