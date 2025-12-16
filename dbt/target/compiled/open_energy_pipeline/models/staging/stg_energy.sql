select
  cast(date as date) as date,
  cast(region as varchar) as region,
  cast(energy_mwh as double) as energy_mwh
from "energy"."main"."raw_energy"