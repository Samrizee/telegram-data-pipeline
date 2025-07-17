
  
    

  create  table "telegram_db"."telegram_db"."fct_image_detections__dbt_tmp"
  
  
    as
  
  (
    

WITH image_data AS (
    SELECT
        message_id,
        detected_object_class,
        confidence_score
    FROM "telegram_db"."telegram_db"."image_detections"  -- Reference your source table
)

SELECT
    message_id,
    detected_object_class,
    confidence_score
FROM image_data
  );
  