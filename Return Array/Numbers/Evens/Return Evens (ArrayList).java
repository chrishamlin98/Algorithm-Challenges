import java.util.Arrays;
import java.util.ArrayList;

public class returnEvens {

  public static void main(String[] args) {
    List<Integer> numbers = {951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980};
  }

  public int evenNumbers (int[]) {
    int resultIndex = 0;
    ArrayList<Integer> input = new ArrayList<>();
    for (int i = 0; i <= input.length - 1; i++) {
        input.add(i % 2 == 0);
    }
  }
}


/*
public class ReturnEvens {

    public static void main(String[] args) {
     int[] numbers = {951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980};
    }
    public int evenNumbers(int[] input) {
      int resultIndex = 0;
     // creating new array //
      int [] result = new int[];
     // looping through array //
      for (int i = 0; i < input.length; i++) {
        // Creating parameters of only even numbers //
        if (input[i] % 2 == 0) {
          result[resultIndex] = input[i];
          resultIndex++;
        }
      }
      return result;
    }
}






// so now the idea is that you want this list to have k[i] added to it
// at each even interval.

List <Rectangle> list1=new ArrayList<Rectangle>();
  list1.add(new Rectangle());

  List<Circle> list2=new ArrayList <Circle>();
  list2.add(new Circle());
  list2.add(new Circle());

  drawShapes(list1);




  public class twoSumArray {

  	public twoSumArray(int[] nums, int target)
      {
  		for(int i = 0; i < nums.length; i++)
          {
              for (int j = i + 1; j < nums.length; j++)
              {
                  if (nums[j] == target - nums[i])
                  {

                  }
              }
          }
      }

      List <Rectangle> list1=new ArrayList<Rectangle>();
      	list1.add(new Rectangle());

      	List<Circle> list2=new ArrayList <Circle>();
      	list2.add(new Circle());
      	list2.add(new Circle());

      	drawShapes(list1);
      	drawShapes(list2);

  	public static void main(String[] args) {
  		ArrayList<Integer>myArray = new ArrayList<Integer>();
  		myArray.add(2);
  		myArray.add(7);
  		myArray.add(11);
  		myArray.add(15);
  		int target = 9;
  		ArrayList<Integer> result = twoSum(myArray,target);
          for(int j : result)
          	System.out.print("["+j+","+target+"]");
  	}
  }
