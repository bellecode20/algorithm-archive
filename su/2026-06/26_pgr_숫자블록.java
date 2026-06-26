import java.util.*;

class Solution {
    public int[] solution(long begin, long end) {
        int length = (int) (end - begin + 1);
        int[] result = new int[length];

        for (long number = begin; number <= end; number++) {
            int index = (int) (number - begin);
            result[index] = getBlockNumber((int) number);
        }

        return result;
    }

    public int getBlockNumber(int number) {
        if (number <= 1) return 0;

        double sqrt = Math.sqrt(number);
        int maxDivisor = 1;

        for (int divisor = 2; divisor <= sqrt; divisor++) {
            if (number % divisor == 0) {
                int pairDivisor = number / divisor;

                if (pairDivisor <= 10_000_000) return pairDivisor;
                if (divisor <= 10_000_000) maxDivisor = Math.max(maxDivisor, divisor);
            }
        }

        return maxDivisor;
    }
}