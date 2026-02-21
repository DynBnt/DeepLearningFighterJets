from PIL import Image
import imagehash
import os

# 1. Créer un dictionnaire pour stocker les empreintes {hash: chemin_image}
hashes = {}
duplicates = []

folderPath = "./dataset/Images/Rafale"

# 2. Parcourir le dossier
for filename in os.listdir(folderPath):
    path = os.path.join(folderPath, filename)
    
    # Charger l'image et calculer le hash
    image = Image.open(path)
    h = str(imagehash.dhash(image))

    # 3. Vérifier si le hash existe déjà
    if h in hashes:
        print(f"[INFO] Doublon trouvé : {filename} est identique à {hashes[h]}")
        duplicates.append(path)
    else:
        hashes[h] = filename

# 4. (Optionnel) Supprimer les doublons
# for path in duplicates: os.remove(path)