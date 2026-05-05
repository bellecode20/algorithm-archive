import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        int totalLen = enemy.length;

        // 최대 힙
        PriorityQueue<Integer> enemyPq = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < totalLen; i++) {
            if (n < enemy[i]) { // 무적권 써야 하는 경우
                if (k == 0) { // 더 이상 무적권 없는 경우
                    return i;
                }

                enemyPq.offer(enemy[i]);

                int maxValue = enemyPq.poll(); // 지금까지 나온 적 중 가장 큰 값
                n += maxValue;                 // 그 라운드는 무적권 쓴 것으로 처리해서 병사 환급
                n -= enemy[i];                 // 현재 라운드 적 처리
                k--;

            } else { // 현재 병사로 막을 수 있는 경우
                enemyPq.offer(enemy[i]);
                n -= enemy[i];
            }
        }

        answer = totalLen;
        return answer;
    }
}