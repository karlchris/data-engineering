{% macro convert_date(column_name) %}

  CONCAT(EXTRACT(YEAR from {{ column_name }} at time zone "UTC"), '-', EXTRACT(MONTH from {{ column_name }} at time zone "UTC"))

{% endmacro %}
