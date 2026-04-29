class Solution {
    public String solution(String number, int k) {
        StringBuilder sb = new StringBuilder();  // 현재 코드에서 스택과 똑같은 역할 수행중
        int n = number.length();
        int targetLength = n - k; // 최종적으로 남겨야 할 숫자의 길이

        for (int i = 0; i < n; i++) {
            char current = number.charAt(i);
            
            // 1. 스택(sb)이 비어있지 않고
            // 2. 아직 지울 기회(k)가 남았으며
            // 3. 스택의 마지막 숫자가 현재 숫자보다 작다면 -> 지우기!
            while (sb.length() > 0 && k > 0 && sb.charAt(sb.length() - 1) < current) {
                sb.deleteCharAt(sb.length() - 1);
                k--;
            }
            
            sb.append(current);
        }

        // 만약 숫자가 내림차순이라 k가 남았다면, 뒤쪽을 잘라줌
        return sb.substring(0, targetLength);
    }
}

// StringBuilder: String은 immutable이라 문자열 자주 수정하거나 반복적으로 합칠 때 사용한다.
// charAt, deleteCharAt, substring