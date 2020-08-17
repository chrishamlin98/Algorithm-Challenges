public boolean isPalindrome(int x) {
		if (x < 0) return false; // if negative
        if (x < 10) return true; // if 0-9

        int reversed = 0;
        int temp = x;
        while (temp > 0) {
            reversed = 10 * reversed + temp % 10;
            temp /= 10;
        }
        return x == reversed;
    }
}
