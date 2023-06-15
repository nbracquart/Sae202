import random

def generate_individual(N):
    """
    Génère une solution aléatoire de N-Reines.
    """
    return [random.randint(0, N-1) for i in range(N)]

def generate_population(N, size):
    """
    Génère une population aléatoire de solutions de N-Reines.
    """
    return [generate_individual(N) for i in range(size)]

def get_conflicts(individual):
    """
    Calcule le nombre de conflits (attaques) sur une solution de N-Reines.
    """
    N = len(individual)
    conflicts = 0
    for i in range(N):
        for j in range(i+1, N):
            if individual[i] == individual[j] or abs(i-j) == abs(individual[i]-individual[j]):
                conflicts += 1
    return conflicts

def get_fitness(individual):
    """
    Calcule le score de fitness d'une solution de N-Reines.
    """
    return 1 / (1 + get_conflicts(individual))

def select_parents(population):
    """
    Sélectionne deux parents aléatoires dans la population en utilisant la roulette de sélection.
    """
    fitnesses = [get_fitness(individual) for individual in population]
    total_fitness = sum(fitnesses)
    selection_probabilities = [fitness / total_fitness for fitness in fitnesses]
    return random.choices(population, weights=selection_probabilities, k=2)

def crossover(parents):
    """
    Croise deux parents pour créer deux enfants en utilisant le croisement en deux points.
    """
    N = len(parents[0])
    point1 = random.randint(1, N-2)
    point2 = random.randint(point1, N-1)
    child1 = parents[0][:point1] + parents[1][point1:point2] + parents[0][point2:]
    child2 = parents[1][:point1] + parents[0][point1:point2] + parents[1][point2:]
    return child1, child2

def mutate(individual):
    """
    Inverse aléatoirement deux positions sur une solution pour la muter.
    """
    N = len(individual)
    i = random.randint
