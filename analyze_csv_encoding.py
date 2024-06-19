import os
import chardet
import csv

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        rawdata = f.read()
        result = chardet.detect(rawdata)
    return result['encoding']

def analyze_csv_encoding(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            encoding = detect_encoding(file_path)
            print(f'File: {file_name}, Encoding: {encoding}')

if __name__ == "__main__":
    folder_path = r'INDIQUEZ LE CHEMIN ABSOLU DU DOSSIER CONTENANT LES FICHIERS CSV'
    analyze_csv_encoding(folder_path)
