from pathlib import Path

# Base project directory (assumes this file lives in src/open_energy_pipeline/)
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
WAREHOUSE_DIR = DATA_DIR / "warehouse"

DUCKDB_PATH = WAREHOUSE_DIR / "energy.duckdb"

# Ensure directories exist
RAW_DIR.mkdir(parents=True, exist_ok=True)
WAREHOUSE_DIR.mkdir(parents=True, exist_ok=True)

# Simple "environment" style config for later extension
class Settings:
    duckdb_path: Path = DUCKDB_PATH

settings = Settings()
