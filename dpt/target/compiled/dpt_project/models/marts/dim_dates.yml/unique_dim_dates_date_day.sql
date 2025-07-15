
    
    

select
    date_day as unique_field,
    count(*) as n_records

from "telegram_db"."telegram_db"."dim_dates"
where date_day is not null
group by date_day
having count(*) > 1


