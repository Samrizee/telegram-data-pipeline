-- tests/no_null_text_messages.sql

select *
from {{ ref('fct_messages') }}
where text is null and has_image = false
