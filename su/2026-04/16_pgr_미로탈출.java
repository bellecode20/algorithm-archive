import java.util.*;

class Solution {
    static int N, M;
    static char[][] map;
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    public int solution(String[] maps) {
        N = maps.length;
        M = maps[0].length();

        map = new char[N][M];

        int sr = 0, sc = 0;
        int lr = 0, lc = 0;
        int er = 0, ec = 0;

        for (int r = 0; r < N; r++) {
            map[r] = maps[r].toCharArray();

            for (int c = 0; c < M; c++) {
                if (map[r][c] == 'S') {
                    sr = r;
                    sc = c;
                } else if (map[r][c] == 'E') {
                    er = r;
                    ec = c;
                } else if (map[r][c] == 'L') {
                    lr = r;
                    lc = c;
                }
            }
        }

        int toLever = bfs(sr, sc, lr, lc);
        if (toLever == -1) {
            return -1;
        }

        int toExit = bfs(lr, lc, er, ec);
        if (toExit == -1) {
            return -1;
        }

        return toLever + toExit;
    }

    private int bfs(int startR, int startC, int goalR, int goalC) {
        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[N][M];

        queue.offer(new int[]{startR, startC, 0});
        visited[startR][startC] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();

            int r = current[0];
            int c = current[1];
            int dist = current[2];

            if (r == goalR && c == goalC) {
                return dist;
            }

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr < 0 || nr >= N || nc < 0 || nc >= M) {
                    continue;
                }

                if (visited[nr][nc]) {
                    continue;
                }

                if (map[nr][nc] == 'X') {
                    continue;
                }

                visited[nr][nc] = true;
                queue.offer(new int[]{nr, nc, dist + 1});
            }
        }

        return -1;
    }
}