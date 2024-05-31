{{ config(materialized='view') }}

select *
from {{ ref('table_sales') }}
where product = 'apple'

union all

select *
from {{ ref('ephemeral_banana_sales') }}
