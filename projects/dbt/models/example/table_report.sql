{{ config(materialized='table') }}

{% set products = ['apple', 'pear', 'banana'] %}

select
    {{ convert_date('date') }} as date,
    {% for product in products %}
        SUM(case when product = '{{ product }}' then quantity * price else 0 end) as {{ product }}_revenue,
    {% endfor %}
    SUM(quantity * price) AS total_revenue
    from {{ ref('table_sales') }}
group by 1
