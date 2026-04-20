import java.io.BufferedReader;
import java.io.InputStreamReader;

// public class Main {
class Main {
    static int N;
    static char[] expression;
    static long answer = Long.MIN_VALUE;

    static long calc(long a, char op, long b) {
        if (op == '+') return a + b;
        if (op == '-') return a - b;
        return a * b;
    }

    static void dfs(int i, long result) {
        if (i >= N) {
            answer = Math.max(answer, result);
            return;
        }

        // 괄호 안 치는 경우
        long noBracket = calc(result, expression[i], expression[i + 1] - '0');
        dfs(i + 2, noBracket);

        // 괄호 치는 경우
        if (i + 3 < N) {
            long yesBracket = calc(expression[i + 1] - '0', expression[i + 2], expression[i + 3] - '0');
            dfs(i + 4, calc(result, expression[i], yesBracket));
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        expression = br.readLine().toCharArray();

        dfs(1, expression[0] - '0');

        System.out.println(answer);
    }
}