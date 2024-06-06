# Dbt test

To achieve high data quality, testing stands as an indispensable component within the data pipeline.
In this context, we will discover the testing framework in dbt, which empowers developers to verify various data metrics in an automated fashion.

## Data test vs. unit test

Before writing a test, let's make sure we understand the distinction between a **data test** and a **unit test**.

- A **data test** is a runtime evaluation conducted within the production pipeline that assesses data quality from various perspectives like freshness and uniqueness.
  It typically runs after the table is updated with the latest data.

!!! example

    For instance, if the source data introduces a new `category` value, the data test should detect the change and send an alert if necessary.

    Its role extends to detecting both data issues coming from the source as well as logic errors within the data warehouse.

- a **unit test** is conducted before deploying the code change to production, and it focuses on testing the transformation logic rather than the data.

!!! note

    During unit test, a dedicated test dataset with expented input and output is prepared instead of using unpredictable production data.

The goal is to identify logic bugs, such as inaccuracies in metric formulas or the absence of a filter before the release.

## testing in dbt

The tests in dbt are `select` statements that search for failing records, records that don't meet certain conditions.

Out of the box, dbt provides a few built-in tests, such as `unique`, `not_null`, `accepted_values`, etc.

The [dbt_utils](https://github.com/dbt-labs/dbt-utils) package provides more advanced tests such as `at_least_one`, `not_null_proportion`, etc. It's also supported by the communities.

Here is an example of the `dbt test`. Tests are defined in the model configuration file.

```yaml
version: 2

models:
  - name: table_sales
    columns:
      - name: quantity
        tests:
          - not_null
      - name: product
        tests:
          - accepted_values:
              values: ["apple", "pear", "banana"]
```

the command to run dbt test is

```bash
dbt test -s <model name>
```

Under the hood, dbt runs the following SQL statement:

```sql
select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
from (

    with all_values as (
        select
            product as value_field,
            count(*) as n_records
        from `<project_id>`.`dbt`.`table_sales`
        group by product

    )
    select *
    from all_values
    where value_field not in (
        'apple','pear','banana'
    )
) dbt_internal_test
```

!!! note

    In most circumstances, the `dbt test` is as important as the model because it validates the data quality at every stage of the pipeline, certainly boosting confidence in data accuracy.

    In addition, dbt provides a common framework for testing, making it easier for teams to collaborate and share knowledge.

If you want to run some example, refer to [Running dbt and Google BigQuery using Docker](../../projects/dbt-bq.md#testing-data-quality)
