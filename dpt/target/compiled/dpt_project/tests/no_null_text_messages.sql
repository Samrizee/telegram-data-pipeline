-- tests/no_null_text_messages.sql

select *
from "telegram_db"."telegram_db"."fct_messages"
where text is null and has_image = false