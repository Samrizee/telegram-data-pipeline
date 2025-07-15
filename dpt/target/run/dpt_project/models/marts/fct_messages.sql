
  create view "telegram_db"."telegram_db"."fct_messages__dbt_tmp"
    
    
  as (
    -- models/marts/fct_messages.sql

with messages as (
    select * from "telegram_db"."telegram_db"."stg_telegram_messages"
)

select
    message_id,
    channel_username as channel_id,
    date::date as date_day,
    text,
    message_length,
    has_image
from messages
  );