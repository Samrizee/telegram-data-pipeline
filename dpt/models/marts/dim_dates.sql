-- models/marts/dim_dates.sql

with dates as (
    select distinct
        date::date as date_day
    from {{ ref('stg_telegram_messages') }}
)

select
    date_day,
    extract(year from date_day) as year,
    extract(month from date_day) as month,
    extract(day from date_day) as day,
    to_char(date_day, 'Day') as day_name,
    to_char(date_day, 'YYYY-MM') as year_month
from dates
