{{ config(materialized='ephemeral') }}

select *
from {{ ref('table_sales') }}
where product = 'banana'
