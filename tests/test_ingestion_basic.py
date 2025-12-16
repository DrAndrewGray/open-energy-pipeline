from datetime import date

from open_energy_pipeline.ingestion.fetch_energy_data import generate_demo_energy_data


def test_generate_demo_energy_data_shape():
    df = generate_demo_energy_data(date(2024, 1, 1), date(2024, 1, 10))
    assert not df.empty
    assert set(df.columns) == {"date", "region", "energy_mwh"}
    assert df["date"].min() == date(2024, 1, 1)
    assert df["date"].max() == date(2024, 1, 10)
