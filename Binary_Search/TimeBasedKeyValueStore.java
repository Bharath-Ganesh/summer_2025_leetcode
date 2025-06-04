package Binary_Search;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Pair implements Comparable<Pair> {

    int timeStamp;
    String value;

    public Pair(String value, int timeStamp) {
        this.timeStamp = timeStamp;
        this.value = value;
    }

    public int compareTo(Pair p) {
        return Integer.compare(this.timeStamp, p.timeStamp);
    }
}

public class TimeBasedKeyValueStore {
    public static void main(String[] args) {
        TimeBasedKeyValueStore timeBasedKeyValueStore = new TimeBasedKeyValueStore();
        timeBasedKeyValueStore.set("foo", "bar", 1);
        System.out.println(timeBasedKeyValueStore.get("foo", 1));
        System.out.println(timeBasedKeyValueStore.get("foo", 1));
        timeBasedKeyValueStore.set("foo", "bar2", 4);
        System.out.println(timeBasedKeyValueStore.get("foo", 4));
        System.out.println(timeBasedKeyValueStore.get("foo", 5));
    }


    Map<String, List<Pair>> timeBasedLookUp;

    public TimeBasedKeyValueStore() {
        timeBasedLookUp = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        List<Pair> timeStamps = timeBasedLookUp.getOrDefault(key, new ArrayList<>());
        timeStamps.add(new Pair(value, timestamp));
        timeBasedLookUp.put(key, timeStamps);
    }

    public String get(String key, int timestamp) {
        if (timeBasedLookUp.containsKey(key)) {
            List<Pair> timeStamps = timeBasedLookUp.get(key);
            return getValue(timestamp, timeStamps);
        }
        return "";
    }

    private String getValue(int timestamp, List<Pair> timeStamps) {

        int low = 0;
        int high = timeStamps.size() - 1;
        String value = "";
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (timeStamps.get(mid).timeStamp == timestamp) {
                return timeStamps.get(mid).value;
            } else if (timeStamps.get(mid).timeStamp < timestamp) {
                value = timeStamps.get(mid).value;
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return value;
    }

}
