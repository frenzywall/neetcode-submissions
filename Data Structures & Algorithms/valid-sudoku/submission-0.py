class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # CRITICAL FIX: Use list comprehension for independent sets
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        squa = [set() for _ in range(9)]

        for i in range(9):        # i is the row index (0 to 8)
            for j in range(9):    # j is the column index (0 to 8)
                item = board[i][j]
                
                if item == ".":
                    continue
                
                # Convert the item to an integer once
                num = int(item)

                # 1. Row Index Check
                if num in rows[i]: return False  # Found a duplicate in the row
                rows[i].add(num)

                # 2. Column Index Check
                if num in cols[j]: return False  # Found a duplicate in the column
                cols[j].add(num)
                
                # 3. 3x3 Sub-box Index Calculation
                # Correct index: (0 to 8)
                sq_index = (i // 3) * 3 + (j // 3)
                
                # 4. Sub-box Check
                if num in squa[sq_index]: return False # Found a duplicate in the box
                squa[sq_index].add(num)
        
        # If the loop completes without finding any duplicates
        return True