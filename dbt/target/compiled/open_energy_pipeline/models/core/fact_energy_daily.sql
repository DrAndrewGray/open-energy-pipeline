select
  date,
  region,
  sum(energy_mwh) as energy_mwh_daily
from "energy"."main_staging"."stg_energy"
group by 1, 2