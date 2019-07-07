/*  Given an array of integers, return indices of the 
two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

*/
//Chris's code//
public static void main(String[] args) {

  int k = 9;
  int [] array = [2, 7, 11, 15];
  for(int i = 0; i<array.length; i++)
  {
    for(int j = 0; j<array.length; i++)
    {  /* Trying to set up the array pointers */
      if (k - array[i] - array[j] == 0)
      { /* This is going to print too many again though */
        return true;
      }
    }
  }


}
/*Chris: so.. I have to create a set up that creates a new array?
ok, so finalize your code to work with the numbers given.. How do you have to change it?  */
gotcha*/

/*Chris: If you have to look back or whatever, just comment out the old and new so we/I can see the
progress of the code.  If you can.  */

/*Nick: The logic is such. You need all your tools laid out before you before you work
on getting a solution. So we know we need a few things. We need our math, we need
an array to put our results into, and that should be about it for this problem.*/

/*Nick: So i needed to check online but this should work what I have below. I just
needed to remember if the i iteration had any code in it.

//Nicklas's code//

public static void main(String[] args) {

  /*So in our main, we're calling our function twoSum with it's required passed in info.*/
  /*We need an array of numbers, and a target number.*/
  /*Now I am not sure why it won't accept nums.length in the below.*/

  twoSum({2,7,11,15}, 9);
}

public int[] twoSum(int[] nums, int target) {

  for(int i = 0; i < nums.length; i++) {
    for (int j = i + 1; j < nums.length; j++) {

    /*We loop through at i + 1 to keep j always ahead of i. Then we establish*/
    /*the math that we need to use to find out if there's 2 numbers that up to target.*/

      if (nums[j] == target - nums[i]) {

      /*We return a new integer array that is created only in the if statement here*/
      /*so that we don't have to use excess memory creating it in global space. This concept*/
      /*is irrelevant right now but is important later.*/
        return new int[] {i, j};
      }
    }
  }
}
