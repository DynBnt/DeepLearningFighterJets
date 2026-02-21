### Méthode 1 : Utilisation de Google Images (Approche semi-manuelle)

Cette méthode repose sur un petit "hack" en JavaScript pour extraire les URLs des images affichées dans votre navigateur.

1. **Recherche :** Allez sur [Google Images](https://images.google.com) et tapez la requête `"f35"`.
2. **Défilement :** Faites défiler la page vers le bas jusqu'à ce que vous ayez chargé suffisamment d'images de l'avion (quelques centaines).
3. **Console JavaScript :** Ouvrez la console de votre navigateur (sur Chrome : `F12` ou `Clic droit > Inspecter > Console`).
4. **Extraction des URLs :** Copiez et collez le code JavaScript fourni dans l'article (qui simule un clic droit sur chaque image pour récupérer son URL réelle). Ce code générera et téléchargera automatiquement un fichier nommé `urls.txt` contenant tous les liens.
5. **Téléchargement via Python :** Utilisez le script Python `download_images.py` présenté dans le tutoriel. Ce script lit le fichier `urls.txt` et utilise la bibliothèque `requests` pour enregistrer chaque image sur votre disque dur dans un dossier nommé `dataset/f35`.

### Méthode 2 : Utilisation de l'API Bing Image Search (Approche rapide et automatique)

C'est la méthode recommandée par l'auteur (Adrian Rosebrock) car elle est entièrement automatisée et plus "propre".

1. **Clé API :** Vous devez d'abord créer un compte gratuit sur Microsoft Cognitive Services pour obtenir une **clé d'API Bing Search**.
2. **Configuration du script :** Prenez le script `search_bing_api.py` fourni dans le second article et insérez votre clé API dans la variable `API_KEY`.
3. **Exécution :** Lancez le téléchargement depuis votre terminal avec la commande suivante :
```bash
python search_bing_api.py --query "f35" --output dataset/f35

```


Le script va automatiquement interroger Bing, récupérer les URLs par lots (groupes de 50) et télécharger les images de F-35 directement dans le dossier spécifié.

### Étapes finales communes (Nettoyage)

Peu importe la méthode choisie, les articles insistent sur deux points cruciaux pour avoir un bon dataset de deep learning :

* **Tri manuel (Pruning) :** Parcourez votre dossier `dataset/f35` et supprimez les images qui ne sont pas des F-35 (par exemple, des graphiques, des jouets, ou d'autres modèles d'avions comme le F-22 qui pourraient s'être glissés dans les résultats).
* **Suppression des doublons :** Vérifiez s'il y a des images identiques pour éviter de biaiser l'entraînement de votre modèle.

**Résumé :** Si vous voulez aller vite et avez une clé Microsoft, utilisez la **méthode Bing**. Si vous ne souhaitez pas créer de compte API, utilisez la **méthode Google Images** avec la console JavaScript.