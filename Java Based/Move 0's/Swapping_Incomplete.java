import java.util.*;

class Solution {
    public void moveZeroes(int[] nums) {
        int i;
        int lastNonZeroFoundAt = 0;
        for (i = 0; i < nums.length(); i++){
            if (nums[i] != 0) {
                swap(nums[lastNonZeroFoundAt++], nums[i]);
            }
        }
    }
}
