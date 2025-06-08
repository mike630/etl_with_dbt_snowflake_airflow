from airflow.sdk import dag, task

@dag
def branch():
    
    @task
    def a():
        return 1
    
    @task.branch
    def b(val: int):
        if val == 1:
            return ["equal_1", "run_if_1"]
        return "different_than_1"
    
    @task
    def equal_1(val: int):
        print(f"Equal to {val}")
        
    @task
    def run_if_1(val: int):
        print(f"Run if {val} is 1")
    
    @task
    def different_than_1(val: int):
        print(f"Different than 1: {val}")
    
    val = a()
    b(val) >> [equal_1(val), different_than_1(val), run_if_1(val)]
    
branch()