import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        int n = numbers.length;
        Integer[] newNums = new Integer[n];
        
        for (int i = 0; i < n; i++) {
            newNums[i] = numbers[i];  // 이렇게 넣는것만으로도 형변환이됨
        }
        
        Arrays.sort(newNums, (a, b) -> {  // int는 오름차순 정렬밖에 안돼서 형바꾼 리스트에서 정렬진행
            String newA = String.valueOf(a);
            String newB = String.valueOf(b);
            
            return (newB + newA).compareTo(newA + newB);  // 내림차순
        });
        StringBuilder sb = new StringBuilder();

        for (int nn: newNums) {  // 반복문
            sb.append(nn);  // 스트링빌더는 그냥 int든 다른 형 추가 가능
        }
        
        if (sb.charAt(0) == '0') {   // 인덱스
            return "0";
        }
        
        return sb.toString();
    }
}