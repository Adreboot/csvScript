import os
import csv
import codecs

def convert_csv_encoding_to_utf8_sig(folder_path):
    # Liste tous les fichiers dans le dossier spécifié
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing file: {file_path}")

            # Vérifie l'encodage actuel du fichier
            with open(file_path, 'r', newline='', encoding='utf-8') as f:
                content = f.read()

            # Réécrit le fichier en UTF-8-SIG avec BOM
            with open(file_path, 'w', newline='', encoding='utf-8-sig') as f:
                f.write(content)

            print(f"Conversion complete for {filename}")

# Exemple d'utilisation
if __name__ == "__main__":
    folder_path = r'INDIQUEZ LE CHEMIN ABSOLU DU DOSSIER CONTENANT LES FICHIERS CSV'
    convert_csv_encoding_to_utf8_sig(folder_path)
