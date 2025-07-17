
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select detection_id
from "telegram_db"."telegram_db"."fct_image_detections"
where detection_id is null



  
  
      
    ) dbt_internal_test