# Delta Lake with Apache Spark: Delta-Spark

![delta-spark](pics/delta-spark.png)

After years of data management, data warehouses reigned supreme with their structured storage and optimized querying.

However, these warehouses struggled when confronted with the deluge of unstructured and semi-structured data, revealing their limitations.
This void led to the emergence of data lakes, offering a promising solution by accommodating diverse data types without immediate structure.

Yet, the initial euphoria surrounding data lakes gave way to challenges of **maintaining data integrity**, **ensuring consistency**, and **handling updates and deletions effectively**.

!!! success

    Enter **Delta Lake**, a technological evolution that seeks to address the shortcomings of traditional data warehouses and data lakes alike.

## What is Delta Lake

**Delta Lake** is an open-source table format for data storage.
Delta Lake improves data storage by supporting ACID transactions, high-performance query optimizations, schema enforcement and evolution, data versioning and many other features.

A Delta table consists of 2 main components:

- **Parquet files** that contain the data, and
- a **transaction log** that stores metadata about the transactions

### Lakehouse Architecture

A **lakehouse** is a new, open architecture that combines the best elements of **data lakes** and **data warehouses**.

Lakehouses are enabled by a new system design: implementing similar data structures and data management features to those in a data warehouse directly on top of low cost cloud storage in open formats.

![lakehouse-architecture](pics/lakehouse-architecture.png)

### Lakehouse Features

- **Transaction support**: many data pipelines will often be reading and writing data concurrently.
- **Schema enforcement and governance**: The Lakehouse should have a way to support the schema enforcement and evolution, supporting DW schema such as star/snowflake-schemas.
- **BI support**: Lakehouses enable using BI tools directly on the source data.
- **Storage is decoupled from compute**: In practice, this means storage and compute use separate clusters, thus these systems are able to scale to many more concurrent users and larger data sizes.
- **Openness**: The storage format they use are open and standardized, such as Parquet, and they provide an API so a variety of tools/engines can efficiently access the data.
- **Support for diverse data types ranging from unstructured and structured data**
- **Support for diverse workloads**: including data science, machine learning, and SQL and analytics.
- **End-to-end streaming**: Real-time reports are the norm in many enterprises. Support for streaming eliminates the need for separate systems dedicated to serving real-time data applications.

## Contents of Delta table

![contents-of-delta-table](pics/contents-of-delta-table.png)

The transaction log enables Delta Lake to optimize the queries, ensure reliable reads and writes, and to store a record of all data transformations.

Delta Lake supports both ETL and ELT workloads.

### Benefits for ETL

Delta Lake is great for **ETL** because of its performance and reliability.

Here are some features that will improve ETL workloads:

#### Query Optimization

Delta Lake makes data transformations faster by:

- storing file paths and metadata in the transaction log
- executing partial reads via file-skipping
- co-locating similar data to allow for better file skipping

!!! tips

    **Transaction logs**
    
    Delta Lake stores all file paths, metadata and data transformation operations in a dedicated transaction log. This makes file listing faster and enables partial data reads.

    **File-skipping**
    
    Delta Lake stores metadata at the file-level in a single transaction log. This way query engines can figure out which data can be skipped using a single network request. Entire files can be skipped this way.

    **Co-locating similar data**
    
    Delta Lake can store similar data close together to improve your query performance, using Z-Ordering or Liquid Clustering.

#### Reliability

Delta Lake makes your ETL workloads more reliable by enforcing ACID transactions. Transactions prevent your data from being corrupted or lost.

!!! example

    Data storage formats without transaction support (like CSV or Parquet) can easily be corrupted. 
    
    For example, if you're writing a large amount of data and your cluster dies then you'll have several partially written files in your table. These partial files will cause downstream read operations to crash.

Delta Lake transactions give you 4 important guarantess:

- **No more failed partial writes**: Every write operation either completes entirely or else it fails entirely and no data gets changed.
- **No more corrupted tables**: If a transaction is going to break any of the pre-defined constraints, the entire transaction is rejected and will not complete.
- **No more conflicting data versions**: Concurrent processes happen in isolation from each other and cannot access each other's intermediate states.
- **No more unintended data loss**: All data changes are guaranteed to never be lost, even in the events of system failures or power outages.

#### Schema Enformement and Evolution

To prevent accidental data corruption, Delta Lake provides schema enforcement.

You cannot write new data to a Delta table if it doesn't match the existing table's schema. It will error out with an `AnalysisException`.

For example, let's create a Delta table with a simple schema:

```python
df = spark.createDataFrame([("bob", 47), ("li", 23), ("leonard", 51)]).toDF(
    "first_name", "age"
)

df.write.format("delta").save("data/toy_data")
```

Now, let's try to write data with a different schema to this same Delta table:

```python
df = spark.createDataFrame([("frank", 68, "usa"), ("jordana", 26, "brasil")]).toDF(
    "first_name", "age", "country"
)

df.write.format("delta").mode("append").save("data/toy_data")
```

Here's the complete error:

```bash
AnalysisException: [_LEGACY_ERROR_TEMP_DELTA_0007] A schema mismatch detected when writing to the Delta table

Table schema:
root
-- first_name: string (nullable = true)
-- age: long (nullable = true)

Data schema:
root
-- first_name: string (nullable = true)
-- age: long (nullable = true)
-- country: string (nullable = true)
```

!!! warning

    Delta Lake does not allow you to append data with mismatched schema by default.

##### Schema Evolution

Of course, ETL workloads evolve over time. Input data may change or your downstream analysis might need a new column. When you need more flexibility in your schema, Delta Lake also supports Schema Evolution.

To update the schema of your Delta table, you can write data with the `mergeSchema` option. Let's try this for the example that we just saw above:

```python
df.write.option("mergeSchema", "true").mode("append").format("delta").save(
    "data/toy_data"
)
```

Here are the contents of your Delta table after the write:

```bash
spark.read.format("delta").load("data/toy_data").show()

+----------+---+-------+
|first_name|age|country|
+----------+---+-------+
|   jordana| 26| brasil| # new
|     frank| 68|    usa| # new
|   leonard| 51|   null|
|       bob| 47|   null|
|        li| 23|   null|
+----------+---+-------+
```

The Delta table now has three columns. It previously only had two columns. Rows that don't have any data for the new column will be marked as null when new columns are added.

#### Time Travel

Nobody is perfect. And no ETL pipeline is perfect, either.

When mistakes happen, you want to be able to roll back your data to a previous version before the mistake. Doing this manually is painful and takes a lot of time. Delta Lake makes this easy by supporting time travel functionality.

Because all of the transactions are stored in the **transaction log**, Delta Lake can always travel back to earlier states of your table.

#### Scalability

ETL workloads often scale up as more data becomes available.
Delta Lake supports both small and very large data workloads.

Delta Lake makes it easier and faster to process large workloads by:

##### Partitioning

![delta-lake-partitioning](pics/delta-lake-partitioning.png)

File partitioning makes it faster to work with data at scale.

In the Query Optimization example we saw above, we used a smart partitioning strategy to make our query run faster. When you partition a table on a certain column, Delta Lake stores all records with the same column value in the same file. This way it can skip entire files when certain column values are not needed.

Partitioning is especially efficient with parallel query engines. In this case, each process (or “worker”) can read its own partitions in parallel. This speeds up your queries and lets you process more data in less time.

##### Data Clustering

Delta Lake lets you store similar data close together via **Liquid Clustering**, **Z-ordering** and **Hive-style partitioning**. Liquid Clustering is the newest and most performant technique of the three.

Your ETL workload will likely benefit from clustering if:

- You often need to filter by high cardinality columns.
- Your data has significant skew in data distribution.
- Your tables grow quickly and require maintenance and tuning effort.
- Your data access patterns change over time.

##### Query Engine Support

Delta Lake makes it easy to work with lots of different query engines.

You might start working locally with a single-node processing library like polars:

```python
# load data
df = pl.DataFrame(data)

# perform some data operations
...

# write to delta table
df.write_delta("data/delta_table")
```

When your data volume increases, you can switch to a distributed query engine like Spark:

```python
# load delta table created with polars
df = spark.read.format("delta").load("data/delta_table")

# join to much larger dataset
big_df = df.join(new_df, …)

# run big data operations
…

# write to delta table
big_df.write.format("delta").mode("append").option("overwriteSchema", "True").save("data/delta_table")
```

!!! info

    Delta Lake has great interoperability with many query engines.

## Optimizing Delta Lake

How to optimize your Delta Lake table to reduce the number of small files.

Small files can be a problem because they slow down your query reads. Listing, opening and closing many small files incurs expensive overhead. This is called **"the Small File Problem"**. You can reduce the Small File Problem overhead by combining the data into bigger, more efficient files.

The code below runs a query on a Delta table with 2 million rows. The Delta table is partitioned on the `education` column and has 1440 files per partition:

```python
%%time
df = spark.read.format("delta").load("test/delta_table_1440")
res = df.where(df.education == "10th").collect()

CPU times: user 175 ms, sys: 20.1 ms, total: 195 ms
Wall time: 16.1 s
```

Now compare this to the same query on the same 2M-rows of data stored in a Delta table with only 1 optimized file per partition:

```python
%%time
df = spark.read.format("delta").load("test/delta_table_1")
res = df.where(df.education == "10th").collect()

CPU times: user 156 ms, sys: 16 ms, total: 172 ms
Wall time: 4.62 s
```

Storing data in an optimized number of files will improve your out-of-the-box read performance.

There are 3 ways you can optimize your Delta Lake table:

### Offline Optimize

### Optimized Write

### Auto Compaction

## Implementation

### Installing Delta Package

### Create delta table

### Read delta table

### Update delta table

#### Overwrite whole table

#### Conditional Update

### Upsert delta table

### Delete delta table

### Read historic data for delta table

## Conclusion

## References

- [Delta Lake Official Documentation](https://delta.io/)
- [What is a Lakehouse?](https://www.databricks.com/blog/2020/01/30/what-is-a-data-lakehouse.html)
- [Delta Lake for ETL](https://delta.io/blog/delta-lake-etl/)
- [Delta Lake Optimize](https://delta.io/blog/delta-lake-optimize/)
- [Delta Lake Introduction](https://medium.com/@ansabiqbal/delta-lake-introduction-with-examples-using-pyspark-cb2a0d7a549d)
