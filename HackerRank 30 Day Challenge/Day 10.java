import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {



    private static final Scanner scanner = new Scanner(System.in);

        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        int count = 0;
        int tempCount = 0;
        while (n>0){
            int remainder = n%2;
            n= n/2;
            if(remainder ==1){
                tempCount++;
                if(tempCount>count){
                    count = tempCount;
                }
            }else{
                tempCount = 0;
            }
        }
        System.out.println(count);
    }
}
