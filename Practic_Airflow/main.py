import pandas
from airflow import DAG
from airflow.models import Variable
# from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from pandas import read_csv


def task_1(**kwargs):
    var = Variable.set("huge_file", "airtravel.csv")
    df = read_csv(Variable.get("huge_file"))
    ti = kwargs["ti"]
    ti.xcom_push("count", df["Month"].count())
    print(df["Month"].count())


def task_2(ti):
    # count = ti.xcom_pull(task_ids="task_1", key="count")
    # df = read_csv(Variable.get("huge_file"))
    df = read_csv("airtravel.csv")
    count = 12
    # temp_arr = [count - i for i in range(1, count)]
    temp_df = pandas.DataFrame({"back-verse": [count - i for i in range(1, count)]})
    df = df.join(temp_df)
    df.to_csv("zdarova.csv")
    print(df)


with DAG(dag_id="my_first_dag", start_date=(2022, 12, 5), schedule="0 0 * * *") as dag:
    task_1 = PythonOperator(
        task_id='task_1',
        python_callable=task_1,
    )

    task_2 = PythonOperator(
        task_id='task_2',
        python_callable=task_2,
    )
    # task_3 = BashOperator(
    #     task_id='task_3',
    #     bash_comand="mv zdarova.csv $AIRFLOW_HOME/zdarova.csv",
    # )
    #
    # task_4 = BashOperator(
    #     task_id='task_3',
    #     bash_comand="echo 'Success'",
    # )
    task_1 >> task_2
    # >> task_3 >> task_4
