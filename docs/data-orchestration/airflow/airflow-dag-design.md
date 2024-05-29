# Airflow DAG Design

To create DAGs, we just need basic knowledge of Python.
However, to create efficient and scalable DAGs, it's essential to master Airflow's specific features and nuances.

## Create a DAG object

A DAG file starts with a `dag` object. We can create a `dag` object using a context manager or a decorator.

```python
from airflow.decorators import dag
from airflow import DAG
import pendulum

# dag1 - using @dag decorator
@dag(
    schedule="30 4 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["random"]
)
def random_dag1():
    pass

random_dag1()

# dag2 - using context manager
with DAG(
    dag_id="random_dag2",
    schedule="@daily",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["random"]
) as dag2:
    pass
```

Either way, we need to define a few parameters to control how a DAG is supposed to run.

Some of the most-used parameters are:

- **start_date**: If it's a future date, it's the timestamp when the scheduler starts to run. If it's a past date, it's the timestamp from which the scheduler will attempt to backfill.

- **catch_up**: Whether to perform scheduler catch-up. If set to true, the scheduler will backfill runs from the start date.

- **schedule**: Scheduling rules. Currently, it accepts a cron string, time delta object, timetable, or list of dataset objects.

- **tags**: List of tags helping us search DAGs in the UI.

## Create a task object

A DAG object is composed of a series of dependent tasks. A task can be an operator, a sensor, or a custom Python function decorated with `@task`.
Then, we will use `>>` or the opposite way, which denotes the **dependencies** between tasks.

```python
# dag3
@dag(
    schedule="30 4 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["random"]
)
def random_dag3():

    s1 = TimeDeltaSensor(task_id="time_sensor", delta=timedelta(seconds=2))
    o1 = BashOperator(task_id="bash_operator", bash_command="echo run a bash script")
    @task
    def python_operator() -> None:
        logging.info("run a python function")
    o2 = python_operator()

    s1 >> o1 >> o2

random_dag3()
```

A task has a well-defined life cycle, including 14 states, as shown in the following graph:

![task life cycle](../pics/task-life-cycle.png)

## Pass data between tasks

One of the best design practices is to split a heavy task into smaller tasks for easy debugging and quick recovery.

!!! example

    we first make an API request and use the response as the input for the second API request.
    To do so, we need to pass a small amount of data between tasks.

**XComs (cross-communications)** is a method for passing data between Airflow tasks.
Data is defined as a key-value pair, and the value must be serializable.

- The `xcom_push()` method pushes data to the Airflow metadata database and is made available for other tasks.

- The `xcom_pull()` method retrieves data from the database using the key.

![example-xcom](../pics/example-xcom.png)

Every time a task returns a value, the value is automatically pushed to XComs.

We can find them in the Airflow UI `Admin` -> `XComs`. If the task is created using `@task`, we can retrieve XComs by using the object created from the upstream task.

In the following example, the operator `o2` uses the traditional syntax, and the operator `o3` uses the simple syntax:

```python
@dag(
    schedule="30 4 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["random"]
)
def random_dag4():

    @task
    def python_operator() -> None:
        logging.info("run a python function")
        return str(datetime.now()) # return value automatically stores in XCOMs
    o1 = python_operator()
    o2 = BashOperator(task_id="bash_operator1", bash_command='echo "{{ ti.xcom_pull(task_ids="python_operator") }}"') # traditional way to retrieve XCOM value
    o3 = BashOperator(task_id="bash_operator2", bash_command=f'echo {o1}') # make use of @task feature

    o1 >> o2 >> o3

random_dag4()
```

!!! warning

    Although nothing stops us from passing data between tasks, the general advice is to not pass heavy data objects, such as pandas DataFrame and SQL query results because doing so may impact task performance.

## Use Jinja templates

!!! info

    Jinja is a templating language used by many Python libraries, such as Flask and Airflow, to generate dynamic content.

    It allows us to embed variables within the text and then have those variables replaced with actual values during runtime.

Airflow's Jinja templating engine provides built-in functions that we can use between double curly braces, and the expression will be evaluated at runtime.

Users can also create their own macros using user_defined_macros and the macro can be a variable as well as a function.

```python
def days_to_now(starting_date):
    return (datetime.now() - starting_date).days

@dag(
    schedule="30 4 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["random"],
    user_defined_macros={
        "starting_date": datetime(2015, 5, 1),
        "days_to_now": days_to_now,
    })
def random_dag5():

    o1 = BashOperator(task_id="bash_operator1", bash_command="echo Today is {{ execution_date.format('dddd') }}")
    o2 = BashOperator(task_id="bash_operator2", bash_command="echo Days since {{ starting_date }} is {{ days_to_now(starting_date) }}")

    o1 >> o2

random_dag5()
```

!!! note

    The full list of built-in variables, macros and filters in Airflow can be found in the [Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html)

Another feature around templating is the `template_searchpath` parameter in the DAG definition.

It's a list of folders where Jinja will look for templates.

!!! example

    A common use case is invoking an SQL file in a database operator such as BigQueryInsertJobOperator. Instead of hardcoding the SQL query, we can refer to the SQL file, and the content will be automatically rendered during runtime.

```python
@dag(
    schedule="30 4 * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["random"],
    template_searchpath=["/usercode/dags/sql"])
def random_dag6():

    BigQueryInsertJobOperator(
        task_id="insert_query_job",
        configuration={
            "query": {
                "query": "{% include 'sample.sql' %}",
                "useLegacySql": False,
            }
        }
    )

random_dag6()
```

## Manage cross-DAG dependencies
