
  
  create view "energy"."main_core"."fact_energy_daily__dbt_tmp" as (
    select
  date,
  region,
  sum(energy_mwh) as energy_mwh_daily
from "energy"."main_staging"."stg_energy"
group by 1, 2
  );
