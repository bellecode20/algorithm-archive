class Solution {
    public int solution(int n, int w, int num) {
        int row = (num - 1) / w;
        int col = (row % 2 == 0) ? (num - 1) % w : (w - 1 - (num - 1) % w);
        int lastRow = (n + w - 1) / w;
        int answer = 0;

        for (int r = row; r < lastRow; r++) {
            int box = (r % 2 == 0) ? r * w + col + 1 : r * w + (w - col);
            if (box <= n) answer++;
        }

        return answer;
    }
}