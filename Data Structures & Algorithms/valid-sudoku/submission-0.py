class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = {}
        rows = {}
        boxes = {(0,0):{}, (1,0):{}, (2,0):{}, (0,1):{}, (0,2):{}, (1,1):{}, (2,2):{}, (1,2):{}, (2,1):{}}
        for i in range(len(board)):
            rows[i] = {}
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if j not in cols:
                    cols[j] = {}
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i][board[i][j]] = True
                if board[i][j] in cols[j]:
                    return False
                else: 
                    cols[j][board[i][j]] = True
                box_key = (int(j/3),int(i/3))
                if board[i][j] in boxes[box_key]:
                    return False
                else: 
                    boxes[box_key][board[i][j]] = True

        return True