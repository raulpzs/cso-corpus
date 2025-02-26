from quantgov.corpus import RecursiveDirectoryCorpusDriver
from pathlib import Path
import os

# Define corpus directory
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR.joinpath('data')

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Initialize corpus driver
driver = RecursiveDirectoryCorpusDriver(
    directory=DATA_DIR,
    index_labels=('filename',)
)

print("✅ Corpus initialized successfully in:", DATA_DIR)