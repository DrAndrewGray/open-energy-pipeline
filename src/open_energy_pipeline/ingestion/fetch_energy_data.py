from datetime import date, timedelta
from typing import List, Dict

import pandas as pd

from open_energy_pipeline.logging_utils import get_logger

logger = get_logger(__name__)


def generate_demo_energy_data(
    start_date: date, end_date: date, region: str = "demo_region"
) -> pd.DataFrame:
    """Generate a small synthetic energy dataset for demo purposes."""
    days: List[date] = []
    current = start_date
    while current <= end_date:
        days.append(current)
        current += timedelta(days=1)

    df = pd.DataFrame(
        {
            "date": days,
            "region": region,
            # Totally fake numbers, but good enough to prove the pipeline
            "energy_mwh": [100 + i * 2 for i in range(len(days))],
        }
    )

    logger.info("Generated %d demo energy rows for region=%s", len(df), region)
    return df
