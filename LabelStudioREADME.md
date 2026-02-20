# 🛰️ Guide d'Installation et d'Utilisation : Label Studio

Ce guide est destiné à notre groupe pour l'annotation des images d'avions de chasse. Suivez bien les étapes pour que nos données soient cohérentes.

---

## 🛠️ 1. Installation

### 🐧 Sur Linux (Ubuntu/Debian)
1. **Ouvrez votre terminal et préparez l'environnement :**
   ```bash
   sudo apt update && sudo apt upgrade -y
   sudo apt install python3 python3-pip python3-venv -y
   mkdir label-studio && cd label-studio
   python3 -m venv ls_env
   source ls_env/bin/activate
   ```
2. **Installez et lancez :**
   ```bash
   pip install label-studio
   label-studio
   ```

### 🪟 Sur Windows
1. **Prérequis :** Installez Python via [python.org](https://www.python.org/) (n'oubliez pas de cocher **"Add Python to PATH"**).
2. **Ouvrez PowerShell ou CMD et tapez :**
   ```powershell
   python -m venv ls_env
   .\ls_env\Scripts\activate
   pip install label-studio
   label-studio
   ```

> **Note :** L'outil s'ouvrira dans le navigateur sur `http://localhost:8080`. Créez un compte (email/password) pour accéder à l'interface.

---

## 🚀 2. Configuration du Projet

1. Cliquez sur **"Create Project"**.
2. Nommez le projet (ex: "DeepLearningFighterJets").
3. **Onglet "Import" :** Glissez-déposez toutes vos images d'avions.
4. **Onglet "Labeling Interface" :**
   * Cliquez sur **Browse Templates**.
   * Choisissez **Computer Vision** -> **Object Detection with Bounding Boxes**.
   * Dans la partie droite (Visual), supprimez les labels par défaut.
   * Ajoutez exactement ces 3 labels :
     * `F35`
     * `Su35`
     * `Rafale`
   * Cliquez sur **Save**.



---

## ✍️ 3. Méthode d'Annotation

1. Cliquez sur le bouton bleu **"Label All Tasks"**.
2. **Sélection :** Cliquez sur le nom de l'avion en bas (ou utilisez les touches **1**, **2**, **3**).
3. **Tracé :** Dessinez un rectangle (Bounding Box) le plus précisément possible autour de l'avion. 
   * *Conseil : Incluez bien les ailes et la queue, mais évitez de prendre trop de décor inutile.*
4. **Validation :** Une fois le rectangle tracé, cliquez sur **Submit** (ou touche `Entrée`).



---

## 📤 4. Exportation (Important)

En attendant le retour du professeur sur le format final (YOLO ou autre), nous allons tout centraliser en CSV.

1. Allez sur la page principale du projet.
2. Cliquez sur le bouton **Export** en haut à droite.
3. Sélectionnez le format **CSV**.
4. Téléchargez le fichier et gardez-le précieusement.

---
