import java.util.*;

class Solution {
    private long[] pow26 = new long[12];
    private long[] prefix = new long[12];

    public String solution(long n, String[] bans) {
        init();

        long[] removed = new long[bans.length];
        for (int i = 0; i < bans.length; i++) {
            removed[i] = strToIndex(bans[i]);
        }

        Arrays.sort(removed);

        long target = n;
        for (long x : removed) {
            if (x <= target) target++;
            else break;
        }

        return indexToStr(target);
    }

    private void init() {
        pow26[0] = 1L;
        for (int i = 1; i <= 11; i++) {
            pow26[i] = pow26[i - 1] * 26L;
        }

        prefix[0] = 0L;
        for (int i = 1; i <= 11; i++) {
            prefix[i] = prefix[i - 1] + pow26[i];
        }
    }

    private long strToIndex(String s) {
        int len = s.length();
        long value = 0L;

        for (int i = 0; i < len; i++) {
            value = value * 26L + (s.charAt(i) - 'a');
        }

        return prefix[len - 1] + value + 1L;
    }

    private String indexToStr(long idx) {
        int len = 1;
        while (prefix[len] < idx) len++;

        long value = idx - prefix[len - 1] - 1L;
        char[] result = new char[len];

        for (int i = len - 1; i >= 0; i--) {
            result[i] = (char) ('a' + (value % 26));
            value /= 26;
        }

        return new String(result);
    }
}