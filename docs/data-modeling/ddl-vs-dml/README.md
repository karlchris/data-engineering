# DDL vs. DML

SQL statements are broadly categorized into two groups: `Data Definition Language (DDL)` and `Data Manipulation Language (DML)`.

## DDL

**DDL** is a set of commands used to create, modify, and delete database objects such as tables, views, indexes, and constraints. Here are a few DDL commands:

- `CREATE`: Create new database objects such as tables.
- `ALTER`: Modify existing database objects such as adding or removing columns from the table.
- `DROP`: Delete a database object such as a table or index.
- `TRUNCATE`: Delete all data from a table without deleting the table itself.
- `RENAME`: Rename an existing database object, like a table or column.

```sql
-- Create table
CREATE TABLE fruits_price (
    fruit varchar(255),
    price float
);
CREATE TABLE exchange_rate (
    from_cur varchar(255),
    to_eur varchar(255),
    rate float
);

-- Add column
ALTER TABLE fruits_price
ADD COLUMN category varchar(255) AFTER price;

-- Drop table
DROP TABLE exchange_rate;

-- Truncate table
TRUNCATE TABLE fruits_price;

-- Rename column
ALTER TABLE fruits_price
CHANGE price price_eur float;
```

## DML

**DML** is a set of commands used to manipulate the data. Here are a few DML commands:

- `SELECT`: Retrieve data from tables or views.
- `INSERT`: Add one or more records to a table.
- `UPDATE`: Modify data of one or more records.
- `DELETE`: Remove one or more records from the table.
- `MERGE`: Handle inserts, updates, and deletes all in a single transaction without writing separate logic for each of these.

```sql
-- Select
SELECT 'Select statement' as '';
SELECT * FROM fruits_price;

-- Insert
SELECT 'INSERT/UPDATE/DELETE statement' as '';
INSERT INTO fruits_price (fruit, price)
VALUES ('blueberry',7.0);

-- Update
UPDATE fruits_price
SET price = 1.5
WHERE fruit = 'apple';

-- Delete
DELETE FROM fruits_price
WHERE fruit = 'banana';
SELECT * FROM fruits_price;

-- MYSQL doesn't support merge, here is the alternative
SELECT 'REPLACE(MERGE) statement' as '';
CREATE TABLE src_fruits_price (
    fruit varchar(255),
    price float
);
INSERT INTO src_fruits_price (fruit, price) -- create a source table
VALUES ('watermelon', 7.0), ('lime', 3.5);
REPLACE INTO fruits_price (fruit, price)
SELECT fruit,price FROM src_fruits_price;
SELECT * FROM fruits_price;
```
