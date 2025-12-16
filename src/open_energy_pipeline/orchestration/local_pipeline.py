import subprocess
from pathlib import Path

from open_energy_pipeline.config import PROJECT_ROOT
from open_energy_pipeline.ingestion.load_to_duckdb import load_demo_energy_data
from open_energy_pipeline.logging_utils import get_logger

logger = get_logger(__name__)


def run_dbt():
    dbt_dir = PROJECT_ROOT / "dbt"
    logger.info("Running dbt from %s", dbt_dir)
    subprocess.run(["dbt", "run"], check=True, cwd=dbt_dir)
    subprocess.run(["dbt", "test"], check=True, cwd=dbt_dir)


def run_pipeline():
    logger.info("Starting local energy pipeline run")

    # Step 1: Ingestion & load into DuckDB
    load_demo_energy_data()

    # Step 2: dbt transformations & tests
    try:
        run_dbt()
    except FileNotFoundError:
        logger.warning(
            "dbt not found on PATH. Install dbt-core to enable transformations."
        )

    logger.info("Pipeline finished.")


if __name__ == "__main__":
    run_pipeline()
