package Binary_Search;

public class MedianOfTwoSortedArrays {

    public static void main(String[] args) {
        MedianOfTwoSortedArrays obj = new MedianOfTwoSortedArrays();
        int[] nums1 = {3, 5, 6, 7};
        int[] nums2 = {2, 4, 4, 8};
        double ans = obj.findMedianSortedArrays(nums1, nums2);
        System.out.println(ans);
    }

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        if(nums1.length > nums2.length){
            return findMedianSortedArrays(nums2, nums1);
        }

        int n1 = nums1.length;
        int n2 = nums2.length;
        int low = 0;
        int high = n1;
        while(low <= high){
            int cut1 = (low + high)/2;
            int cut2 = (n1 + n2 + 1)/2 - cut1;

            int leftA   =   cut1 == 0  ? Integer.MIN_VALUE : nums1[cut1 - 1];
            int leftB   =   cut2 == 0  ? Integer.MIN_VALUE : nums2[cut2 - 1];
            int rightA  =   cut1 == n1 ? Integer.MAX_VALUE : nums1[cut1];
            int rightB  =   cut2 == n2 ? Integer.MAX_VALUE : nums2[cut2];

            if(leftA <= rightB && leftB <= rightA){
                // even
                if((n1 + n2) % 2 == 0){
                    return (Math.max(leftA, leftB) + Math.min(rightA, rightB))/2.0;
                }else {
                    return 1.0 * Math.max(leftA, leftB);
                }
            }else if(leftA > rightB){
                high = cut1 - 1;
            }else {
                low = cut1 + 1;
            }
        }
        return 0.0;
    }
}

