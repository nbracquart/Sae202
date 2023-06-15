import random

def generate_board(n):
    """
    Génère un plateau aléatoire de taille n x n.
    """
    board = [[0] * n for i in range(n)]
    for i in range(n):
        j = random.randint(0, n-1)
        board[i][j] = 1
    return board

def get_conflicts(board):
    """
    Calcule le nombre de conflits (attaques) sur le plateau.
    """
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                # Vérifie les conflits sur la ligne
                for k in range(n):
                    if k != j and board[i][k] == 1:
                        conflicts += 1
                
                # Vérifie les conflits sur la colonne
                for k in range(n):
                    if k != i and board[k][j] == 1:
                        conflicts += 1
                
                # Vérifie les conflits sur la diagonale supérieure gauche
                k, l = i-1, j-1
                while k >= 0 and l >= 0:
                    if board[k][l] == 1:
                        conflicts += 1
                    k -= 1
                    l -= 1
                
                # Vérifie les conflits sur la diagonale inférieure gauche
                k, l = i+1, j-1
                while k < n and l >= 0:
                    if board[k][l] == 1:
                        conflicts += 1
                    k += 1
                    l -= 1
                
                # Vérifie les conflits sur la diagonale supérieure droite
                k, l = i-1, j+1
                while k >= 0 and l < n:
                    if board[k][l] == 1:
                        conflicts += 1
                    k -= 1
                    l += 1
                
                # Vérifie les conflits sur la diagonale inférieure droite
                k, l = i+1, j+1
                while k < n and l < n:
                    if board[k][l] == 1:
                        conflicts += 1
                    k += 1
                    l += 1
    
    return conflicts // 2  # Chaque conflit est compté deux fois.

def get_min_conflicts_pos(board, row):
    """
    Retourne la position de la colonne avec le nombre minimum de conflits pour la ligne donnée.
    """
    n = len(board)
    min_conflicts = n**2
    min_pos = -1
    for j in range(n):
        if board[row][j] == 1:
            # Ignore les positions déjà occupées
            continue
        
        board[row][j] = 1
        conflicts = get_conflicts(board)
        if conflicts < min_conflicts:
            min_conflicts = conflicts
            min_pos = j
        board[row][j] = 0
    
    return min_pos

def solve_n_queens(n, max_iter=1000):
    """
    Résout le problème des reines en utilisant l'algorithme de recherche locale.
