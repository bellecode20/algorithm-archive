import java.util.*;

class Solution {
    public int solution(int[] cards) {
        boolean[] visited = new boolean[cards.length];
        List<Integer> groups = new ArrayList<>();

        for (int i = 0; i < cards.length; i++) {
            if (visited[i]) continue;

            int count = 0;
            int cur = i;

            while (!visited[cur]) {
                visited[cur] = true;
                cur = cards[cur] - 1;
                count++;
            }

            groups.add(count);
        }

        if (groups.size() < 2) return 0;

        groups.sort(Collections.reverseOrder());
        return groups.get(0) * groups.get(1);
    }
}
