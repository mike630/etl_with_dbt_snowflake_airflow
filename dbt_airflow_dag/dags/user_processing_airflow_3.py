# // This code is for an Airflow DAG that uses new python syntax with decorators for Airflow 3.x


from airflow.sdk import dag, task
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.sdk.bases.sensor import PokeReturnValue
from airflow.providers.postgres.hooks.postgres import PostgresHook
    
@dag
def user_processing_new_airflow_3():
    
    create_table = SQLExecuteQueryOperator(
        task_id="create_table",
        conn_id="postgres",
        sql="""
        CREATE TABLE IF NOT EXISTS users (
            id INT,
            firstname VARCHAR(255),
            lastname VARCHAR(255),
            email VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    
    @task.sensor(poke_interval=30, timeout=300)
    def is_api_available() -> PokeReturnValue:
        import requests
        response = requests.get("https://raw.githubusercontent.com/marclamberti/datasets/refs/heads/main/fakeuser.json")
        print(response.status_code)
        if response.status_code == 200:
            condition = True
            fake_user = response.json()
        else:
            condition = False
            fake_user = None
        return PokeReturnValue(is_done=condition, xcom_value=fake_user)
    
    @task
    def extract_user(fake_user):
        
        from datetime import datetime
        
        dict_data_user = {
            "id": fake_user["id"],
            "firstname": fake_user["personalInfo"]["firstName"],
            "lastname": fake_user["personalInfo"]["lastName"],
            "email": fake_user["personalInfo"]["email"],
            "created_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return dict_data_user
        
    @task
    def process_user(dict_data_user):
        
        import csv
        
        cols = ["id", "firstname", "lastname", "email", "created_at"]
        
        with open('/tmp/processed_user.csv', 'w', newline='') as csvfile:
            
            writer = csv.DictWriter(csvfile, fieldnames=cols)
            # writer.writeheader() # Write headers
            writer.writerow(dict_data_user) # Write data
            
        return 'CSV file created successfully'
    
    @task
    def store_user():
        hook = PostgresHook(postgres_conn_id='postgres')
        hook.copy_expert(
            sql="COPY users FROM STDIN WITH DELIMITER AS ','",
            filename='/tmp/processed_user.csv'
        )
    
    
    fake_user = is_api_available()
    
    create_table >> fake_user 
    dict_data_user = extract_user(fake_user)
    process_user_object = process_user(dict_data_user)
    process_user_object >> store_user()
    
user_processing_new_airflow_3()