from ruamel import yaml

import great_expectations as ge
from great_expectations.core.batch import RuntimeBatchRequest

GCP_PROJECT_NAME = "data-engineering-424915"
BIGQUERY_DATASET = "data_eng"


# Instantiate project DataContext
context = ge.get_context()

# Configure Datasource
datasource_config = {
    "name": "my_bigquery_datasource",
    "class_name": "Datasource",
    "execution_engine": {
        "class_name": "SqlAlchemyExecutionEngine",
        "connection_string": f"bigquery://{GCP_PROJECT_NAME}/{BIGQUERY_DATASET}",
    },
    "data_connectors": {
        "default_runtime_data_connector_name": {
            "class_name": "RuntimeDataConnector",
            "batch_identifiers": ["default_identifier_name"],
        },
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetSqlDataConnector",
            "include_schema_name": True,
        },
    },
}
context.test_yaml_config(yaml.dump(datasource_config))

# Save Datasource configuration to DataContext
context.add_datasource(**datasource_config)

# Test new Datasource
batch_request = RuntimeBatchRequest(
    datasource_name="my_bigquery_datasource",
    data_connector_name="default_runtime_data_connector_name",
    data_asset_name="table_sales",  # this can be anything that identifies this data
    runtime_parameters={"query": "SELECT * from data_eng.table_sales LIMIT 10"},
    batch_identifiers={"default_identifier_name": "default_identifier"},
)

context.add_or_update_expectation_suite(
    expectation_suite_name="test_suite"
)
validator = context.get_validator(
    batch_request=batch_request, expectation_suite_name="test_suite"
)
print(validator.head())

# Data Quality checks
validator.expect_column_values_to_not_be_null("quantity")

validator.expect_column_values_to_not_be_null("product")
validator.expect_column_values_to_be_in_set(
    "product",
    ["apple", "pear", "banana",],
)

validator.expect_column_values_to_not_be_null("price")
validator.expect_column_values_to_be_between(
    "price", min_value=0, max_value=None,
)
validator.save_expectation_suite(discard_failed_expectations=False)

# Run checkpoint
checkpoint = context.add_or_update_checkpoint(
    name="my_quickstart_checkpoint",
    validator=validator,
)
checkpoint_result = checkpoint.run()
context.view_validation_result(checkpoint_result)
