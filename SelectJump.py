import numpy as np

# Charger le fichier txt
# Remplacer 'trajectoire.txt' par le chemin vers ton fichier
name = input('input name:')
data = np.loadtxt(name)

# Séparer les colonnes
temps = data[:, 0]
positions = data[:, 1]

# Définir les valeurs du saut, la tolérance, et le nombre de pas après b
a = 3.0  # Remplacer par la valeur de 'a'
b = 2.7  # Remplacer par la valeur de 'b'
tol = 0.01  # Tolérance pour détecter des valeurs proches de 'a' et 'b'
steps_before_a = 0#100000  # Nombre de pas de temps avant l'arrivée à 'a'
steps_after_b = 0#500000   # Nombre de pas de temps après l'arrivée à 'b'

# Trouver tous les indices où la position est proche de 'a' et 'b'
indices_a = np.where(np.abs(positions - a) < tol)[0]
indices_b = np.where(np.abs(positions - b) < tol)[0]

# Rechercher le premier 'b' (proche)
end_index = -1
start_index = -1

if len(indices_b) > 0:
    # On prend le premier indice où la position est proche de b
    end_index = indices_b[0]

    # Ensuite, on remonte pour trouver la dernière occurrence de 'a' avant b
    for i in reversed(indices_a):
        if i < end_index:  # Trouver le dernier 'a' avant b
            start_index = i
            break

# Si un saut a été trouvé
if start_index != -1 and end_index != -1:
    # Calculer l'indice initial en soustrayant steps_before_a à start_index
    initial_index = max(start_index - steps_before_a, 0)  # S'assurer que l'on ne va pas avant le début des données

    # Calculer l'indice final en ajoutant steps_after_b à end_index
    final_index = min(end_index + steps_after_b, len(temps) - 1)  # S'assurer que l'on ne dépasse pas la fin des données

    # Extraire la partie de la trajectoire entre 'initial_index' et 'final_index'
    filtered_temps = temps[initial_index:final_index + 1]
    filtered_positions = positions[initial_index:final_index + 1]

    filtered_temps = filtered_temps - filtered_temps[0]
    
    # Sauvegarder les données filtrées dans un fichier texte
    filtered_data = np.column_stack((filtered_temps, filtered_positions))
    np.savetxt('plotjump'+name, filtered_data, fmt='%f', delimiter='\t')

    # Afficher les données filtrées
    print(filtered_data)
else:
    print("Aucun saut de a à b trouvé avec la tolérance définie.")