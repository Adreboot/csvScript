# analyse_csv_encoding.py : Analyseur d'encodage de fichiers CSV

Ce script Python permet de détecter l'encodage des fichiers CSV dans un dossier spécifié. Il utilise la bibliothèque `chardet` pour détecter l'encodage des fichiers.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir installé les bibliothèques nécessaires. Vous pouvez les installer en utilisant `pip` :

```bash
pip install chardet
```

## Utilisation
1. **Modifier le chemin du dossier** : Remplacez `INDIQUEZ LE CHEMIN ABSOLU DU DOSSIER CONTENANT LES FICHIERS CSV` par le chemin absolu du dossier contenant vos fichiers CSV dans le script Python.
2. **Exécution du script** : Lancez le script en utilisant la commande suivante :

```bash
python analyse_csv_encoding.py
```

__________________________________________________________________________________________________________

# changeEncodeToUTF8SIG.py : Convertisseur d'encodage de fichiers CSV en UTF-8-SIG

Ce script Python permet de convertir l'encodage des fichiers CSV dans un dossier spécifié en UTF-8-SIG (avec BOM).

## Utilisation

1. **Modifier le chemin du dossier** : Remplacez `INDIQUEZ LE CHEMIN ABSOLU DU DOSSIER CONTENANT LES FICHIERS CSV` par le chemin absolu du dossier contenant vos fichiers CSV dans le script Python.

2. **Exécution du script** : Lancez le script en utilisant la commande suivante :

```bash
python changeEncodeToUTF8SIG.py
```