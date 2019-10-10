package Challenges;

import java.io.*;
import java.util.*;

public class day6 {

	/*
	String myString = "This is String example.";
	char[] myCharArray = myString.toCharArray();
	for(int i = 0; i < myString.length(); i++){
	    // Print each sequential character on the same line
	    System.out.print(myCharArray[i]);
	}
	// Print a newline
	System.out.println();
	 */
	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		int i, t, j;
		String e="", o="";

		t=scanner.nextInt();

		String []s = new String[t];

		for(i=0;i<t;i++)
		{
			s[i]=scanner.next();

			char c[]=s[i].toCharArray();

			for(j=0;j<s[i].length();j++)
			{
				if(j%2==0)
				{
					e+=c[j];
				}
				else
				{
					o+=c[j];
				}
			}
			System.out.println(e+" "+o);
			e="";o="";
		}
		scanner.close();
	}
}
