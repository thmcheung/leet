class Solution {
    public boolean kLengthApart(int[] nums, int k) {
        int cur = 0;
        int flag = 0;
        for (int i = 0; i < nums.length; i ++){
            if (flag == 1 && nums[i] != 1){
                cur ++;
            }
            if (nums[i] == 1){
                if (flag == 1){
                    if (cur < k){
                        return false;
                    }
                }
                flag = 1;
                cur = 0;
            }
        }
        return true;
    }
}