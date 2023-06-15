def is_valid(board, row, col):
    """
    Vérifie si la position (row, col) est valide pour placer une reine sur le plateau.
    """
    # Vérifie la colonne
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Vérifie la diagonale supérieure gauche
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Vérifie la diagonale supérieure droite
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    # La position est valide
    return True


def solve_n_queens(board, row):
    """
    Résout le problème des reines en utilisant l'algorithme de backtracking.
    """
    # Cas de base : toutes les reines ont été placées
    if row == len(board):
        return True
    
    # Place une reine sur chaque colonne de la ligne actuelle
    for col in range(len(board)):
        if is_valid(board, row, col):
            # Place la reine sur le plateau
            board[row][col] = 1
            
            # Récursivement essaye de placer les reines sur les rangées suivantes
            if solve_n_queens(board, row + 1):
                return True
            
            # Si la configuration actuelle n'a pas fonctionné, retire la reine
            board[row][col] = 0
    
    # Aucune configuration ne fonctionne
    return False


def print_solution(board):
    """
    Affiche la solution sous forme de tableau.
    """
    for row in board:
        print(row)


# Exemple d'utilisation
n = 8  # nombre de reines
board = [[0] * n for i in range(n)]
if solve_n_queens(board, 0):
    print_solution(board)
else:
    print("Aucune solution trouvée.")
