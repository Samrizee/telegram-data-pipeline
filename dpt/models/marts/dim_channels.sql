-- models/marts/dim_channels.sql

with messages as (
    select * from {{ ref('stg_telegram_messages') }}
)

select distinct
    channel_username as channel_id,
    channel_username as channel_name  
from messages
where channel_username is not null
