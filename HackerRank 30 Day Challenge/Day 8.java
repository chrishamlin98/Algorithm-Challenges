//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

/*

// Create a Map of String Keys to String Values, implemented by the HashMap class
Map<String,String> myMap = new HashMap<String,String>();

// Adds ("Hi","Bye") mapping to myMap
myMap.put("Hi", "Bye");

// Print the Value mapped to from "Hi"
System.out.println(myMap.get("Hi"));

// Replaces "Bye" mapping from "Hi" with "Bye!"
myMap.put("Hi", "Bye!");

// Print the Value mapped to from "Hi"
System.out.println(myMap.get("Hi"));

containsKey(Object key): Returns true if the map contains a mapping for ; returns false if there is no such mapping.
get(Object key): Returns the value to which the  is mapped; returns null if there is no such mapping.
put(K key, V value): Adds the (Key, Value) mapping to the Map; if the  is already in the map, the  is overwritten.

*/

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Map<String, Integer> myMap = new HashMap<String, Integer>();

        for(int i = 0; i < n; i++){
            String name = in.next();
            int phone = in.nextInt();

            myMap.put(name, phone);
        }
        while(in.hasNext()){
            String s = in.next();
            if(myMap.containsKey(s))
            {
                System.out.println(s + "=" + myMap.get(s));
            } else {
                System.out.println("Not found");
            }
        }
        in.close();
    }
}
