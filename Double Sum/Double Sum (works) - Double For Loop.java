class Program {
  public static int[] twoNumberSum(int[] array, int targetSum) {
    for (int i = 0; i < array.length; i++) {
			int numberOne = array[i];
			for (int j = i + 1; j < array.length; j++) {
				int numberTwo = array[j];
				if (array[i] + array[j] == targetSum)
					return new int[] {numberOne, numberTwo};
			}
		}
		return new int[0];
  }
}
