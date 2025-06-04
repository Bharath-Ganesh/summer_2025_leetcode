package Backtracking;

public class WordSearch {

    public static void main(String[] args) {
        WordSearch obj = new WordSearch();
        char[][] board = {
                {'A','B','C','E'},
                {'S','F','E','S'},
                {'A','D','E','E'}
        };
        String word = "ABCESEEEFS";
        boolean ans = obj.exist(board, word);
        System.out.println(ans);
    }

    public boolean exist(char[][] board, String word) {

        if(board == null) return false;
        if(word == null || word.isEmpty()) return true;

        int rows = board.length;
        int cols = board[0].length;
        boolean visited[][] = new boolean[rows][cols];
        for(int row = 0; row < rows; row++){
            for(int col = 0; col < cols; col++){

                if(board[row][col] == word.charAt(0)){
                    if(searchForWord(board, row, col, 0, visited, word)){
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private boolean searchForWord(char[][] board, int row, int col, int index, boolean[][] visited, String word){

        if(row < 0 || col < 0 || row >= board.length || col >= board[0].length || visited[row][col] || board[row][col] != word.charAt(index)){
            return false;
        }
        if(index == word.length() - 1){
            return true;
        }
        visited[row][col] = true;
        // we found the character
        if(board[row][col] == word.charAt(index)){
            // D, R, L, U
            if(searchForWord(board, row + 1, col, index + 1, visited,  word)
                    || searchForWord(board, row, col + 1, index + 1, visited, word)
                    || searchForWord(board, row, col - 1, index + 1, visited, word)
                    || searchForWord(board, row - 1, col, index + 1, visited, word))
            {
                return true;
            }
        }else {
            if(searchForWord(board, row + 1, col, index, visited, word)
                    || searchForWord(board, row, col + 1, index, visited, word)
                    || searchForWord(board, row, col - 1, index, visited, word)
                    || searchForWord(board, row - 1, col, index, visited, word))
            {
                return true;
            }

        }
        visited[row][col] = false;
        return false;

    }
}
