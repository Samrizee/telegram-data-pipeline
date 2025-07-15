
  create view "telegram_db"."telegram_db"."stg_telegram_messages__dbt_tmp"
    
    
  as (
    -- models/staging/stg_telegram_messages.sql

with raw as (
    select * from "telegram_db"."raw"."telegram_messages"
)

select
    id as message_id,
    channel_username,
    text,
    date,
    media_path,
    
    -- Derived fields
    case 
        when media_path is not null then true
        else false
    end as has_image,

    length(text) as message_length

from raw
where id is not null
  );