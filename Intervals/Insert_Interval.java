package Intervals;

import java.util.ArrayList;
import java.util.List;

public class Insert_Interval {

    public static void main(String[] args) {
        Insert_Interval insert_interval = new Insert_Interval();
        int[][] intervals = {{1,3},{6,9}};
        int[] newInterval = {2,5};
        int[][] result = insert_interval.insert(intervals, newInterval);
        for(int[] interval : result){
            for(int val : interval){
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }

    public int[][] insert(int[][] intervals, int[] newInterval) {
        /*
            intervals = [** [2,3],**[6,9]], newInterval = [2,5]
            [0,1],
            [4,5]
            [2,7]
        */
        List<int[]> res = new ArrayList<>();

        int start = newInterval[0]; //2
        int end = newInterval[1];  // 5
        for(int index = 0; index < intervals.length; index++){
            // For the example [0,1]
            // 5 < 1
            if(end < intervals[index][0]){
                res.add(new int[]{start, end});
                for(int currIndex = index; currIndex < intervals.length; currIndex++){
                    res.add(intervals[currIndex]);
                }
                return constructFinalResult(res);
            }
            // 2 > 3
            // For the example [4,5]
            else if(start >  intervals[index][1]){
                res.add(intervals[index]);
            }
            // For the example [2,5]

            else {
                start   = Math.min(start, intervals[index][0]);
                end     = Math.max(end, intervals[index][1]);
            }
        }
        res.add(new int[]{start, end});
        return constructFinalResult(res);
    }

    private int[][] constructFinalResult(List<int[]> res){
        int size = res.size();
        int[][] finalResult = new int[size][2];
        for(int index = 0; index < size; index++){
            finalResult[index] = res.get(index);
        }
        return finalResult;
    }
}
