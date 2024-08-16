import re
import os

# Définition des expressions régulières pour identifier les commandes en français
conversion_patterns = {
    'Tourne droite de': 'right',
    'Tourne gauche de': 'left',
    'Avance': 'forward',
    'Recule': 'backward'
}

# Fonction pour convertir les commandes françaises en anglais pour Turtle
def convert_commands(input_file_path, output_file_path):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            converted_line = line
            for french_command, english_command in conversion_patterns.items():
                if french_command in line:
                    # Extraire la valeur numérique après la commande
                    match = re.search(rf'{french_command} (\d+)', line)
                    if match:
                        value = match.group(1)
                        # Construire la nouvelle ligne en anglais
                        converted_line = f"{english_command} {value}\n"
                        break
            outfile.write(converted_line)

# Définir les chemins des fichiers
input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'turtle')
output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'turtle_converted')

# Exécuter la conversion
convert_commands(input_file_path, output_file_path)
