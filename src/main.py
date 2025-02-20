import sys

def main():
    from src.config import DATA_DIR
    print(f"Le dossier des données est : {DATA_DIR}")

# 1) Si on exécute directement : __name__ == "__main__" ET __spec__ est None
if __name__ == "__main__" and __spec__ is None:
    print("\n❌ ERROR: This script must be run as a module.")
    print("Use: `python -m src.main` instead of `python src/main.py`.\n")
    sys.exit(1)

# 2) Si on exécute en mode -m : __name__ == "__main__" MAIS __spec__ n'est pas None
#    → on exécute alors main()
if __name__ == "__main__":
    main()