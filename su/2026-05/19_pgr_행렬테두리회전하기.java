class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[][] board = new int[rows][columns];
        int value = 1;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                board[i][j] = value++;
            }
        }

        int[] answer = new int[queries.length];

        for (int i = 0; i < queries.length; i++) {
            int x1 = queries[i][0] - 1;
            int y1 = queries[i][1] - 1;
            int x2 = queries[i][2] - 1;
            int y2 = queries[i][3] - 1;

            int prev = board[x1][y1];
            int min = prev;

            for (int y = y1 + 1; y <= y2; y++) {
                int temp = board[x1][y];
                board[x1][y] = prev;
                prev = temp;
                min = Math.min(min, prev);
            }

            for (int x = x1 + 1; x <= x2; x++) {
                int temp = board[x][y2];
                board[x][y2] = prev;
                prev = temp;
                min = Math.min(min, prev);
            }

            for (int y = y2 - 1; y >= y1; y--) {
                int temp = board[x2][y];
                board[x2][y] = prev;
                prev = temp;
                min = Math.min(min, prev);
            }

            for (int x = x2 - 1; x >= x1; x--) {
                int temp = board[x][y1];
                board[x][y1] = prev;
                prev = temp;
                min = Math.min(min, prev);
            }

            answer[i] = min;
        }

        return answer;
    }
}