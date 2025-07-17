
    
    

select
    detection_id as unique_field,
    count(*) as n_records

from "telegram_db"."telegram_db"."fct_image_detections"
where detection_id is not null
group by detection_id
having count(*) > 1


