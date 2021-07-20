class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        for(int i = 0 ; i<phone_book.length ; i ++){
            for(int j = 0 ; j<phone_book.length-i ; j++){
                if(i!=i+j) {
                    if (phone_book[i].startsWith(phone_book[i+j])) answer = false;
                    if (phone_book[j+i].startsWith(phone_book[i])) answer = false;
                }
            }
            if(!answer) break;
        }

        return answer;
    }
}