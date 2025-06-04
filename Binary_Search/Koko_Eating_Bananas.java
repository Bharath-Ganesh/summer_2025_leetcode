package Binary_Search;

import java.util.Arrays;

public class Koko_Eating_Bananas {

    public static void main(String[] args) {
        Koko_Eating_Bananas koko_eating_bananas = new Koko_Eating_Bananas();
        int ans = koko_eating_bananas.minEatingSpeed(new int[]{3,6,7,11}, 8);
        System.out.println(ans);
    }

    public int minEatingSpeed(int[] piles, int h) {

        int low = 1;
        int high = Arrays.stream(piles)
                .boxed()
                .max(Integer::compare)
                .orElseThrow();
        int minAnswer = high + 1;
        while(low <= high){
            int speed = low + (high - low) / 2;
            boolean isPossible = checkIfSpeedPossible(piles, h, speed);
            if(isPossible){
                minAnswer = speed;
                high = speed - 1;
            }else{
                low = speed + 1;
            }
        }
        return minAnswer;
    }

    private boolean checkIfSpeedPossible(int[] piles, int minHours, int speed){

        int hours = 0;
        for(int pile : piles){
            hours += ((pile + speed - 1)/speed);
            if(hours > minHours){
                return false;
            }
        }
        return hours <= minHours;
    }
}
