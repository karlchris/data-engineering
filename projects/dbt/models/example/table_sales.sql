{{ config(materialized='table') }}

select 'apple' as product, 10 as quantity, 1.0 as price, TIMESTAMP('2023-01-01') as date
union all 
select 'pear' as product, 5 as quantity, 2.0 as price, TIMESTAMP('2023-01-01') as date
union all
select 'banana' as product, 7 as quantity, 3.0 as price, TIMESTAMP('2023-01-01') as date
