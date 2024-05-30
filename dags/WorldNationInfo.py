from airflow import DAG
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator

from datetime import datetime
from datetime import timedelta

dag = DAG(
    dag_id = 'S3_to_Redshift',
    start_date = datetime(2024,4,30), # 날짜가 미래인 경우 실행이 안됨
    schedule = '0 9 * * *',  # 적당히 조절
    max_active_runs = 1,
    catchup = False,
    default_args = {
        'retries': 1,
        'retry_delay': timedelta(minutes=3),
    }
)

schema = "yonggu_choi_14"
table = "nation_info"
s3_bucket = "yonggu-practice-bucket"
s3_key = "nation-info"       # s3_key = schema + "/" + table

s3_to_redshift_nps = S3ToRedshiftOperator(
    task_id = 's3_to_redshift_nation_info',
    s3_bucket = s3_bucket,
    s3_key = s3_key,
    schema = schema,
    table = table,
    column_list = ["country", "area", "population"],
    copy_options=["csv", "IGNOREHEADER AS 1", "QUOTE AS '\"'", "DELIMITER ','"],
    redshift_conn_id = "redshift_dev_db",
    aws_conn_id = "aws_conn_id_choi",
    method = "UPSERT",
    upsert_keys = ["country"],
    dag = dag
)

s3_to_redshift_nps
