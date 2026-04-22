import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Main {
// public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        String bomb = br.readLine();

        int n = s.length();
        int m = bomb.length();

        char[] stack = new char[n];
        int top = 0;

        char last = bomb.charAt(m - 1);

        for (int i = 0; i < n; i++) {
            char cur = s.charAt(i);
            stack[top++] = cur;

            // 마지막 문자가 같고, 길이가 충분할 때만 검사
            if (cur == last && top >= m) {
                boolean isBomb = true;

                for (int j = 0; j < m; j++) {
                    if (stack[top - m + j] != bomb.charAt(j)) {
                        isBomb = false;
                        break;
                    }
                }

                if (isBomb) {
                    top -= m; // 폭발 문자열 길이만큼 제거
                }
            }
        }

        if (top == 0) {
            System.out.println("FRULA");
        } else {
            System.out.println(new String(stack, 0, top));
        }
    }
}