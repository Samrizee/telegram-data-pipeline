
  create view "telegram_db"."telegram_db"."dim_dates__dbt_tmp"
    
    
  as (
    -- models/marts/dim_dates.sql

with dates as (
    select distinct
        date::date as date_day
    from "telegram_db"."telegram_db"."stg_telegram_messages"
)

select
    date_day,
    extract(year from date_day) as year,
    extract(month from date_day) as month,
    extract(day from date_day) as day,
    to_char(date_day, 'Day') as day_name,
    to_char(date_day, 'YYYY-MM') as year_month
from dates
  );