package leetcode;

class PalindromeNumber {

    public boolean isPalindrome(int x) {
        String asString = Integer.toString(x);
        int n = asString.length();
        for (int i = 0; i < n / 2; i++) {
            if (asString.charAt(i) != asString.charAt(n - i - 1)) {
                return false;
            }
        }
        return true;
    }
}
