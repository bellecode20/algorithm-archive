class Solution {
    public int solution(int n, int[] stations, int w) {
        int answer = 0;
        int cover = 2 * w + 1; // 기지국 1개가 커버하는 범위
        int prev = 1; // 이전 기지국 커버 끝 + 1

        for (int station : stations) {
            int left = station - w; // 현재 기지국 커버 시작
            if (left > prev) {
                int gap = left - prev; // 커버 안 되는 구간 길이
                answer += (gap + cover - 1) / cover; // 올림 나눗셈
            }
            prev = station + w + 1; // 현재 기지국 커버 끝 + 1
        }

        // 마지막 기지국 이후 ~ N 구간 처리
        if (prev <= n) {
            int gap = n - prev + 1;
            answer += (gap + cover - 1) / cover;
        }

        return answer;
    }
}