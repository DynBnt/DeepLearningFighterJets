import os
from ddgs import DDGS
from fastdownload import download_url
from pathlib import Path
from time import sleep
from PIL import Image


def search_and_download(keywords, max_images=100, output_dir="../../dataset/Images"):
    dest = Path(output_dir)
    dest.mkdir(exist_ok=True, parents=True)

    with DDGS() as ddgs:
        for category in keywords:
            print(f"Recherche : {category}...")
            category_dir = dest / category
            category_dir.mkdir(exist_ok=True)

            try:

                results = ddgs.images(category, region="wt-wt", max_results=max_images)

                count = 0
                for i, res in enumerate(results):
                    try:
                        file_path = category_dir / f"{i:04d}.jpg"
                        download_url(res['image'], file_path, timeout=10)
                        sleep(1)
                        count += 1
                    except Exception:
                        continue
                print(f"{count} images récupérées pour {category}")

            except Exception as e:
                print(f"Erreur sur {category} : {e}")
                continue


def verify_images(image_dir):
    path = Path(image_dir)
    for img_path in path.rglob("*.jpg"):
        is_valid = True
        try:
            with Image.open(img_path) as img:
                img.verify()

            with Image.open(img_path) as img:
                width, height = img.size
                if width < 200 or height < 200:
                    is_valid = False
                    print(f"Trop petit : {img_path.name} ({width}x{height})")
        except Exception:
            is_valid = False
            print(f"Non conforme : {img_path.name}")

        if not is_valid:
            img_path.unlink()


def stats_dataset(image_dir):
    path = Path(image_dir)
    print("\n" + "=" * 30)
    print("BILAN DU DATASET")
    print("=" * 30)

    total = 0
    for folder in path.iterdir():
        if folder.is_dir():
            count = len(list(folder.glob("*.jpg")))
            total += count
            print(f"{folder.name.ljust(10)} : {count} images")

    print("-" * 30)
    print(f"TOTAL : {total} images valides")
    print("=" * 30)


# Liste d'avions
avions = ["F35", "Rafale", "Su35"]
search_and_download(avions,max_images=300)

# Nettoyage des images
verify_images("../../dataset/Images")

# Bilan de la récup d'images
stats_dataset("../../dataset/Images")