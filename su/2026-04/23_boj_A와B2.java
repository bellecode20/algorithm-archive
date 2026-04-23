import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    static String S, T;

    static int dfs(String txt) {
        if (txt.length() == S.length()) {
            return txt.equals(S) ? 1 : 0;
        }

        if (txt.charAt(txt.length() - 1) == 'A') {
            if (dfs(txt.substring(0, txt.length() - 1)) == 1) {
                return 1;
            }
        }

        if (txt.charAt(0) == 'B') {
            String next = new StringBuilder(txt.substring(1)).reverse().toString();
            if (dfs(next) == 1) {
                return 1;
            }
        }

        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        S = br.readLine().trim();
        T = br.readLine().trim();

        System.out.println(dfs(T));
    }
}