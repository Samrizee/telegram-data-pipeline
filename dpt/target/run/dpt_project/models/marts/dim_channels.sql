
  create view "telegram_db"."telegram_db"."dim_channels__dbt_tmp"
    
    
  as (
    -- models/marts/dim_channels.sql

with messages as (
    select * from "telegram_db"."telegram_db"."stg_telegram_messages"
)

select distinct
    channel_username as channel_id,
    channel_username as channel_name  
from messages
where channel_username is not null
  );