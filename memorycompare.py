import psutil
import subprocess

# Lancer le script ribolegoat.py
process = subprocess.Popen(['python', 'ribolegoat.py'])

# Attendre que le script se termine
process.wait()

# Mesurer la quantité de mémoire utilisée
memory_usage = process.memory_info().rss

print(f"La mémoire utilisée est de {memory_usage / 1024 / 1024:.2f} Mo.")
