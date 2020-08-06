import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> hashMap = new HashMap<String, Integer>();

        for(String i : completion){
            if(hashMap.containsKey(i)){
                hashMap.put(i,hashMap.get(i)+1);
            }
            else {
                hashMap.put(i,1);
            }
        }

        String result = null;
        for(String i : participant){
            if(!hashMap.containsKey(i)){
                result = i;
                break;
            }
            if(hashMap.get(i)>1){
                hashMap.put(i,hashMap.get(i)-1);
            }
            else{
                hashMap.remove(i);
            }
        }
        
        return result;

    }
}