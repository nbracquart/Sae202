def solve_n_queens_recursive(n):
    """
    Résout le problème des n reines en utilisant une approche récursive.
    """
    def is_valid(board, row, col):
        """
        Vérifie si une position est valide (ne cause pas de conflit avec les reines déjà placées).
        """
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True
    
    def solve(board, row):
        """
        Résout le problème des n reines pour la ligne donnée en utilisant une approche récursive.
        """
        if row == n:
            # Toutes les reines ont été placées, la solution est trouvée.
            return board
        
        # Essaye de placer une reine sur chaque colonne de la ligne actuelle.
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                # Appelle la fonction récursivement pour placer la reine sur la ligne suivante.
                solution = solve(board, row + 1)
                if solution:
                    return solution
        # Aucune position valide n'a été trouvée pour la reine sur cette ligne, retourne None.
        return None
    
    # Appelle la fonction solve avec une liste vide pour initialiser le plateau et la première ligne.
    return solve([None] * n, 0)
