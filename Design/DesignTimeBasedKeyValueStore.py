from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.lookUp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.lookUp[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.lookUp:
            return ""
        return self.findValue(self.lookUp[key], timestamp)

    def findValue(self, arr, timestamp):
        low, high = 0, len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid][1] == timestamp:
                return arr[mid][0]
            elif arr[mid][1] < timestamp:
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return "" if ans == -1 else arr[ans][0]
if __name__ == '__main__':
    # Your TimeMap object will be instantiated and called as such:
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)
    print(timeMap.get("foo", 1))
    print(timeMap.get("foo", 3))
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))
    print(timeMap.get("foo", 5))