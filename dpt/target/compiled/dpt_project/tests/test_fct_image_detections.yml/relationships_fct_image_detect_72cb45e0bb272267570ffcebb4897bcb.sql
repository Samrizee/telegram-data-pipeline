
    
    

with child as (
    select message_id as from_field
    from "telegram_db"."telegram_db"."fct_image_detections"
    where message_id is not null
),

parent as (
    select message_id as to_field
    from "telegram_db"."telegram_db"."fct_messages"
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


