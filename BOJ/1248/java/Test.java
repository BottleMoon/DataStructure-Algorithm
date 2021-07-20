// 첫 문제 풀이. 무식하게 경우의 수 하나하나 다 대입하려다 보니 재귀가 너무 깊어서 스택오버플로우 에러가 났다. 
public class Test {
    public static void main(String[] args) {
        final int N = Integer.parseInt(args[0]);    //수열 원소의 개수
        final char[] charArray = args[1].toCharArray(); //ex) +--++0-+
        int[] nArr = new int[N];
        for( int i = 0; i <N ; i++){
            nArr[i] = -10;
        }
        int[] result = cases(nArr,N-1,charArray,N);
        for(int i : result) System.out.print(i+" ");


    }
    private static int[] cases(int [] nArr, int n,char[] charArray,int N){
        int[] result = new int[N];
        if(n == N-1){
            for(;nArr[n] <10; nArr[n] ++){
                if(sum(nArr,charArray,N)) result = nArr;
            }
            if(sum(nArr,charArray,N)) result = nArr;
            cases(nArr,n-1,charArray,N);
        }
        else if(n <N-1){
            if(nArr[n] <10 && nArr[n+1] == 10){
                for(int i = n+1;i<N; i++){
                    nArr[i] = -10;
                }
                nArr[n] ++;
                cases(nArr,N-1,charArray,N);
            }
            else if(nArr[n] == 10 && n != 0){
                cases(nArr,n-1,charArray,N);
            }
            if(nArr[0] == 10 ) return result;
        }
        return result;
    }

    private static boolean sum(int[] intArray, char[] charArray, int N){
        int count = 0;
        for(int i1 = 0 ; i1 < N ; i1++){
            for(int i2 = i1; i2 <N; i2 ++){
                int sum= 0;
                for(int i3 = i1 ; i3 <=i2; i3++){         //i~j까지의 합
                    sum += i1;
                }
                count ++;
                if(!check(sum, count, charArray)){
                    return false;
                }
            }
        }
        return true;
    }

    private static boolean check(int sum, int count, char[] charArray) {
        count --;
        if (charArray[count] == '+'){
            if(sum > 0) return true;
            else return false;
        }
        if(charArray[count] == '-'){
            if(sum < 0) return true;
            else return false;
        }
        else{
            if(sum == 0) return true;
            else return false;
        }
    }
}

