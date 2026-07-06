import java.util.*;

class Solution {
    static class Task {
        String name;
        int start;
        int left;

        Task(String name, int start, int left) {
            this.name = name;
            this.start = start;
            this.left = left;
        }
    }

    public String[] solution(String[][] plans) {
        List<Task> tasks = new ArrayList<>();
        for (String[] plan : plans) {
            tasks.add(new Task(plan[0], toMin(plan[1]), Integer.parseInt(plan[2])));
        }

        tasks.sort(Comparator.comparingInt(t -> t.start));

        Stack<Task> stack = new Stack<>();
        List<String> answer = new ArrayList<>();

        for (int i = 0; i < tasks.size() - 1; i++) {
            Task cur = tasks.get(i);
            Task next = tasks.get(i + 1);

            int available = next.start - cur.start;

            if (cur.left <= available) {
                answer.add(cur.name);
                available -= cur.left;

                while (available > 0 && !stack.isEmpty()) {
                    Task prev = stack.pop();
                    if (prev.left <= available) {
                        answer.add(prev.name);
                        available -= prev.left;
                    } else {
                        prev.left -= available;
                        stack.push(prev);
                        available = 0;
                    }
                }
            } else {
                cur.left -= available;
                stack.push(cur);
            }
        }

        answer.add(tasks.get(tasks.size() - 1).name);
        while (!stack.isEmpty()) {
            answer.add(stack.pop().name);
        }

        return answer.toArray(new String[0]);
    }

    private int toMin(String time) {
        String[] t = time.split(":");
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }
}