// Create a string of letters where the system will print out the reverse order
of the letters//

/* This was as far as I got
  public static reverse[](String word) {
      String word[] = new word;
        for (
}
*/
// ****************************************************Attempt 1

class ReverseString {
	public static void main(String[] args) {
		String x = "Yabba Dabba";
		System.out.println(i);
	}

	public void input(String input) {
		byte[] strAsByteArray = input.getBytes();
		byte[] results = new byte[strAsByteArray.length];
		for (int i = 0; i < strAsByteArray.length; i++)
			result[i] = strAsByteArray(strAsByteArray.length - i - 1);
	}
	

**************************************

// This code has an error on the last strAsByteArray - It says that the method
//is undefined

	class ReverseString {
		public static void main(String[] args) {
			String x = "Yabba Dabba";
			System.out.println(new String(x));
		}

		public void input(String input) {
			byte[] strAsByteArray = input.getBytes();
			byte[] result = new byte[strAsByteArray.length];
			for (int i = 0; i < strAsByteArray.length; i++) {
				result[i] = strAsByteArray(strAsByteArray.length - i - 1);
			}
		}
}
