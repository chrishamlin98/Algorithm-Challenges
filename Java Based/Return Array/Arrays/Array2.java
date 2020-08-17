// This was my first array run through of this type to be done
// without any assistance. It took 3 tries to get it right.

public class Array2 {

		public static void main(String[] args) {
			// Step 1: Create a main method with an array to input
			int[] nums = {2, 4, 6, 8, 10};
			// Step 3: Create a statement to run the loop through the main method
			change(nums);
			// Step 4: Enhanced for loop creating a variable to run through and sysout
			for( int y: nums)
				System.out.println(y);
		}

		public static void change(int x[]) {
			// Step 2: Create the for loop with the operation to be completed
			for(int i = 0; i < x.length; i++) {
				x[i]/=2;
			}
		}
}
