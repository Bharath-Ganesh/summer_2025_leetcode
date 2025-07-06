from typing import List


class Solution:
    def carFleetaproach2(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        position = [10,8,0,5,3]   speed = [2,4,1,1,3]
        pairs → [(0,1),(3,3),(5,1),(8,4),(10,2)]
        times  → [10, (10-8)/4=0.5, …]
        """
        distance_speed = []
        for i in range(len(speed)):
            distance_speed.append((position[i], speed[i]))

        distance_speed.sort(key=lambda x: x[0])

        time_stack = []
        while distance_speed:
            distance, spd = distance_speed.pop()
            time_taken = (target - distance) / spd

            # ---- FIXED LOGIC BELOW ----
            # only start a new fleet if this car takes longer than
            # the fleet ahead; otherwise it merges (do nothing).
            if not time_stack or time_taken > time_stack[-1]:
                time_stack.append(time_taken)
            # else: time_taken <= time_stack[-1] → merges into existing fleet

        return len(time_stack)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        position = [10,8,0,5,3], => 10 8
           speed = [2, 4,1,1,3]
         =>  [0, 3,5,8,10]
         =>  [1, 3,1,4, 2]
         =>   11  3   1 1
        """
        distance_speed = []
        for i in range(len(speed)):
            distance_speed.append((position[i], speed[i]))

        distance_speed.sort(key=lambda x: x[0])

        time_stack = []
        while distance_speed:
            distance, spd = distance_speed.pop()
            time_taken = (target - distance) / spd
            time_stack.append(time_taken)
            while time_stack and time_stack[-1] >= time_taken:
                time_stack.pop()

        return len(time_stack)

if __name__ == '__main__':
    s = Solution()
    ans = s.carFleetaproach2(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])
    print(ans)