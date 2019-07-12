package dcp4_28_19;

import java.nio.charset.Charset;
// Don't forget the import!! //

public class ReverseString3 {

    private static byte[] reverse(byte[] bytes) {
    	/* This code takes the array locations of the characters you are
    	reversing and splits it in half.  If it is an even numbered array
    	then it swaps the locations of the characters from the outside in
    	and if it is an odd number then the center character becomes the pivot.
    	(ie)
    	h e l l o
    	- - l - -
    	o - l - h
    	o l l e h
    	*/
        for (int i = 0; i < bytes.length / 2; i++) {
            byte b1 = bytes[i];
            bytes[i] = bytes[bytes.length - 1 - i];
            bytes[bytes.length - 1 - i] = b1;
        }

        return bytes;
    }

    public static void main(String[] args) {
    	/*
    	 This main method labels the character set to use for byte storage
    	 and correctly calls the reversed string.
    	 */
        String toReverse = "Yabba Dabba";

        byte[] reversedStringData = toReverse.getBytes(Charset.forName("UTF-8"));

        System.out.println(new String(reversedStringData));

        byte[] reversed = reverse(reversedStringData);

        System.out.println(new String(reversed));
    }
}
