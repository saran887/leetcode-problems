import java.io.*;
import java.lang.*;
import java.util.*;
 
class Solution{
    
    public boolean containsDuplicate(int[] nums) {
        
        HashSet<Integer> set = new HashSet<>();
        
        for(int i = 0; i<nums.length;i++){
            set.add(nums[i]);
        }
        
        // if it contains duplicate then the size of 
        // set will not equal to the length
        // of the array
        if(set.size() < nums.length)
            return true;
        
        return false;
    }
    
	public static void main (String[] args) {
	    
	    Solution sol= new Solution();
	    
	    int nums[]= {1, 2, 3, 1};
	    
	    boolean res = sol.containsDuplicate(nums);
	    
	    System.out.println(res);
	}
}