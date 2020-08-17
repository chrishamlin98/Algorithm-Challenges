 import java.util.*;

class Solution {
    public void moveZeroes(int[] nums) {
        int i;
        int[] array = new int[5];
        for (i = 0; i < array.length; i++){
            if (array[i] == 0) {
             
/* ShrinedToday at 6:07 PM
@chamlin I think starting off, you should loop through the array finding any non-zero integers. use one variable  (we'll call it counter) that only increases everytime a new element is found, and the variable in your for loop, in this case "i", should iterate every check and when a non-zero is found you set arr[counter] = arr[i]. After that is traversed, you could use another for loop that starts at where the counter variable ended, and adds 0's until it reaches the end of the array
time complexity is O(N*2) or O(N), there might be a more optimal solution... then later, you're replacing the number of 0's there was originally */             

/*     public static void zeroAtEnd(int arr[]){
        int counter = 0;
        for(int i = 0; i < arr.length; i++){
            if (arr[i] != 0){
                arr[counter] = arr[i];
                counter++;}
        }
    }             
            }
        }
        return;
        }
            
    }
 
 and then after, you're going to want to put all the zeros at the end
well, this is how i did it
