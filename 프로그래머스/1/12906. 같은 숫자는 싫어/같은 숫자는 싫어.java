import java.util.*;

public class Solution {
    public List solution(int []arr) {
        List v = new ArrayList();
        
        v.add(arr[0]);
        
        for (int i = 1; i<arr.length; i++){
            // 이전 수와 비교 했을 때 다르다면 추가하기
            if (arr[i] != arr[i-1]) {
                v.add(arr[i]);               
            }
        }
        
        // System.out.println(v);
        
        return v;
    }
}