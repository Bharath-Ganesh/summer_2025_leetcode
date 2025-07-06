from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        [numPassengersi, fromi, toi]
         trips = [[2,1,5],[3,3,7]], # Lets sort it by the from location

            start,end
            [1,   5] => [5, 3, 7]


            start,end
            [3,  7]
        """
        if not trips or len(trips) <= 1:
            return True
        prev_passenger, prev_start, prev_end = trips[0]
        for i in range(1, len(trips)):
            trip = trips[i]
            passenger, start, end = trip
            # we need to car pool
            if prev_end > start:
                prev_passenger = passenger + prev_passenger
                if prev_passenger > capacity:
                    return False
                prev_end = max(prev_end, end)
            else:
                # passengers got off
                prev_passenger, prev_start, prev_end = passenger, start, end

        return True

if __name__ == '__main__':
    s = Solution()
    ans = s.carPooling([[2,2,6],[2,4,7],[8,6,7]], capacity = 11)
    print(ans)