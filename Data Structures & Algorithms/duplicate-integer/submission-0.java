class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> f = new HashSet<>();
    
        for(int num: nums){
            if(f.contains(num)){
                return true;
            }else{
                f.add(num);
            }
        }
        return false;
        
    }
}