def n_queens(n):
    solutions = [0]
    cols = []
    main_diag = []
    anti_diag = []
    
    def backtrack(row):
        if row == n:
            solutions[0] += 1
            return
        
        for col in range(n):
            # проверяем, не бьёт ли ферзя
            if col in cols or (row + col) in main_diag or (row - col) in anti_diag:
                continue
            
            # ставим ферзя
            cols.append(col)
            main_diag.append(row + col)
            anti_diag.append(row - col)
            
            backtrack(row + 1)
            
            # убираем ферзя (назад)
            cols.pop()
            main_diag.pop()
            anti_diag.pop()
    
    backtrack(0)
    return solutions[0]
