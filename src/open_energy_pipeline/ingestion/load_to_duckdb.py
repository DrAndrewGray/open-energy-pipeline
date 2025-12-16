from datetime import date

import duckdb
from open_energy_pipeline.config import settings
from open_energy_pipeline.ingestion.fetch_energy_data import generate_demo_energy_data
from open_energy_pipeline.logging_utils import get_logger

logger = get_logger(__name__)


def load_demo_energy_data():
    logger.info("Connecting to DuckDB at %s", settings.duckdb_path)
    con = duckdb.connect(str(settings.duckdb_path))

    # Generate some demo data
    df = generate_demo_energy_data(
        start_date=date(2024, 1, 1),
        end_date=date(2024, 1, 31),
        region="demo_region",
    )

    # Create raw table and insert data
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS raw_energy (
            date DATE,
            region VARCHAR,
            energy_mwh DOUBLE
        );
        """
    )

    con.execute("DELETE FROM raw_energy;")  # idempotent demo load
    con.execute("INSERT INTO raw_energy SELECT * FROM df", {"df": df})

    logger.info(
        "Loaded %d rows into raw_energy in DuckDB",
        con.execute("SELECT COUNT(*) FROM raw_energy").fetchone()[0],
    )

    con.close()


if __name__ == "__main__":
    load_demo_energy_data()
