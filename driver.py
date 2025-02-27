import quantgov as qg
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

driver = qg.corpus.RecursiveDirectoryCorpusDriver(
    directory=BASE_DIR.joinpath('data', 'clean'),  # Adjusted path
    index_labels=('filename',)  # Using filename as index
)