import java.util.*;

class Solution {
    public static int[] solution(String[] genres, int[] plays) {
        int[] answer;
        List<Integer> answerList = new ArrayList<>();
        Map<String, Integer> genresAndPlay = new HashMap<>();
        List<String> sortedGenres = new ArrayList<>();
        List<Map<Integer, Integer>> genresList = new ArrayList<Map<Integer, Integer>>();
        int i = 0;
        for(String s : genres){
            if(genresAndPlay.containsKey(s)){ genresAndPlay.put(s,genresAndPlay.get(s)+plays[i]); }
            else{ genresAndPlay.put(s,plays[i]); }
            i++;
        }
        for(Map.Entry<String,Integer> m : sortStringMapByValue(genresAndPlay)) {
            sortedGenres.add(m.getKey());
        }

        for(String s : sortedGenres){
            int j =0;
            Map<Integer,Integer> temp = new HashMap<>();
            for(i = 0; i < genres.length; i ++){
                if(s.equals(genres[i])){
                    temp.put(i,plays[i]);
                }
                System.out.println();
            }
            genresList.add(temp);
        }

        for(Map<Integer,Integer> m : genresList){
            int j= 0;
            for(Map.Entry<Integer,Integer> e : sortIntegerMapByValue(m)){
                answerList.add(e.getKey());
                j ++;
                if(j==2) break;
            }
        }

        answer = new int[answerList.size()];
        i = 0;
        for(int j : answerList){
            answer[i] = j;
            i ++;
        }
        return answer;
    }

    //Map<String,Integer>의 오름차순 정렬
    public static List<Map.Entry<String,Integer>> sortStringMapByValue(Map<String,Integer> map){
        List<Map.Entry<String,Integer>> mapList = new LinkedList<>(map.entrySet());
        Collections.sort(mapList, new Comparator<Map.Entry<String, Integer>>() {
            @Override
            public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
                return o2.getValue().compareTo(o1.getValue());
            }
        });
        return mapList;
    }

    //Map<Integer,Integer>의 내림차순 정렬
    public static List<Map.Entry<Integer,Integer>> sortIntegerMapByValue(Map<Integer,Integer> map){
        List<Map.Entry<Integer,Integer>> mapList = new LinkedList<>(map.entrySet());
        Collections.sort(mapList, new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) {
                return o2.getValue().compareTo(o1.getValue());
            }
        });
        return mapList;
    }
}