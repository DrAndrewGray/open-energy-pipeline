
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select date
from "energy"."main_staging"."stg_energy"
where date is null



  
  
      
    ) dbt_internal_test