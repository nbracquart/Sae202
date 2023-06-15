import time
import subprocess

# Lancer le script ribolegoat.py
start_time = time.time()
subprocess.run(['python', 'ribolegoat.py'])
end_time = time.time()

# Calculer le temps d'exécution
execution_time = end_time - start_time

print(f"Le temps d'exécution est de {execution_time:.2f} secondes.")