class Solution {
    private int zeroCount = 0;
    private int oneCount = 0;

    public int[] solution(int[][] arr) {
        quadCompress(arr, 0, 0, arr.length);
        return new int[]{zeroCount, oneCount};
    }

    private void quadCompress(int[][] arr, int r, int c, int size) {
        if (isUniform(arr, r, c, size)) {
            if (arr[r][c] == 0) {
                zeroCount++;
            } else {
                oneCount++;
            }
            return;
        }

        int nextSize = size / 2;
        quadCompress(arr, r, c, nextSize);
        quadCompress(arr, r, c + nextSize, nextSize);
        quadCompress(arr, r + nextSize, c, nextSize);
        quadCompress(arr, r + nextSize, c + nextSize, nextSize);
    }

    private boolean isUniform(int[][] arr, int r, int c, int size) {
        int val = arr[r][c];
        for (int i = r; i < r + size; i++) {
            for (int j = c; j < c + size; j++) {
                if (arr[i][j] != val) {
                    return false;
                }
            }
        }
        return true;
    }
}