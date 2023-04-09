from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

default_args = {
  'owner': 'airflow'
}
with DAG(
    dag_id="test",
    start_date=days_ago(1),
    schedule_interval="@once",
    default_args=default_args,
    catchup=False,
) as dag:
  populate_country = PostgresOperator(
    task_id='populate_country',
    postgres_conn_id='postgres_default',
    sql='sql/country.sql',
    dag=dag
  )
  populate_country