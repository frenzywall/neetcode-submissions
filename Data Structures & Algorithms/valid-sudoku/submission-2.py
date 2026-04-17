class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        squa = [set() for _ in range(9)]

        for i in range(9):      
            for j in range(9):    
                item = board[i][j]
                
                if item == ".":
                    continue
                
                num = int(item)

                if num in rows[i]: return False  # Found a duplicate in the row
                rows[i].add(num)

                if num in cols[j]: return False  # Found a duplicate in the column
                cols[j].add(num)
                sq_index = (i // 3) * 3 + (j // 3)
                
                if num in squa[sq_index]: return False # Found a duplicate in the box
                squa[sq_index].add(num)
        
        return True