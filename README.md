# Data Pipeline Project

This is a **dbt** project for building and managing data pipelines. The project is designed to work with the **Snowflake** data warehouse and leverages the TPCH dataset for demonstration purposes.

## Project Structure

- **`models/`**: Contains dbt models.
  - **`staging/`**: Includes staging models for the TPCH dataset, such as `stg_tpch_orders.sql`.
  - **`marts/`**: Reserved for business logic and aggregated data models.
- **`analyses/`**: Placeholder for analysis queries.
- **`macros/`**: Placeholder for custom macros.
- **`seeds/`**: Placeholder for seed data.
- **`snapshots/`**: Placeholder for snapshot definitions.
- **`tests/`**: Placeholder for custom tests.
- **`target/`**: Stores compiled and executed artifacts (ignored by Git).

## Current Features

1. **Source Configuration**:
   - Configured the TPCH dataset as a source in `tpch_source.yml`.
   - Includes tests for `orders` and `lineitem` tables, such as:
     - `unique` and `not_null` tests for `o_orderkey`.
     - `relationships` test between `lineitem.l_orderkey` and `orders.o_orderkey`.

2. **Staging Models**:
   - `stg_tpch_orders.sql`: A staging model that selects all columns from the `orders` table in the TPCH dataset.

3. **Materialization**:
   - Staging models are materialized as **views**.
   - Mart models (future development) will be materialized as **tables**.

## Getting Started

### Prerequisites

- Install dbt: [Installation Guide](https://docs.getdbt.com/docs/installation)
- Set up a Snowflake account and configure your dbt profile.

### Running the Project

1. Run the following commands to execute the project:
   ```bash
   dbt run
# Data Pipeline Project

This project integrates **dbt**, **Apache Airflow**, and **Snowflake** to build and manage data pipelines. It leverages the TPCH dataset for demonstration purposes and provides an end-to-end workflow for data transformation and orchestration.

## Project Structure

- **`dags/`**: Contains Airflow DAGs for orchestrating dbt workflows.
  - **`dbt_dag.py`**: Defines a DAG that runs dbt commands using the `cosmos` library and integrates with Snowflake.
- **`dbt/`**: Contains dbt project files for data transformation.
  - **`data_pipeline/`**: Includes dbt models, configurations, and dependencies.
    - **`dbt_project.yml`**: Main configuration file for the dbt project.
    - **`models/`**: Contains dbt models.
      - **`staging/`**: Includes staging models for the TPCH dataset, such as `stg_tpch_orders.sql`.
      - **`marts/`**: Reserved for business logic and aggregated data models.
    - **`packages.yml`**: Specifies dbt dependencies.
- **`tests/`**: Contains unit tests for Airflow DAGs and dbt models.
  - **`test_dag_example.py`**: Ensures all DAGs have proper configurations and no import errors.
- **`Dockerfile`**: Defines the runtime environment for Airflow and dbt, including the installation of `dbt-snowflake`.
- **`requirements.txt`**: Lists Python dependencies, including `astronomer-cosmos` and `apache-airflow-providers-snowflake`.

## Features

### Airflow Integration
- **DAG Orchestration**: The `dbt_dag.py` file defines a DAG that orchestrates dbt commands using the `cosmos` library.
- **Snowflake Integration**: Airflow connects to Snowflake using the `snowflake_conn` connection ID.
- **Custom Environment**: A virtual environment (`dbt_venv`) is created within the Airflow container to run dbt commands.

### dbt Transformations
1. **Source Configuration**:
   - Configured the TPCH dataset as a source in `tpch_source.yml`.
   - Includes tests for `orders` and `lineitem` tables, such as:
     - `unique` and `not_null` tests for `o_orderkey`.
     - `relationships` test between `lineitem.l_orderkey` and `orders.o_orderkey`.

2. **Staging Models**:
   - `stg_tpch_orders.sql`: A staging model that selects all columns from the `orders` table in the TPCH dataset.

3. **Materialization**:
   - Staging models are materialized as **views**.
   - Mart models (future development) will be materialized as **tables**.

### Testing
- **Airflow DAG Tests**:
  - `test_dag_integrity_default.py`: Validates the integrity of all DAGs and ensures no import errors.
  - `test_dag_example.py`: Ensures all DAGs have tags, retries set to two, and no import errors.
- **dbt Model Tests**:
  - Includes built-in tests for uniqueness, nullability, and relationships.

## Getting Started

### Prerequisites
- Install Docker and Docker Compose.
- Install dbt: [Installation Guide](https://docs.getdbt.com/docs/installation).
- Set up a Snowflake account and configure your dbt profile.

### Running the Project

1. Start the Airflow environment:
   ```bash
   astro dev start
   ```
   This will spin up the necessary Docker containers for Airflow.

2. Access the Airflow UI at [http://localhost:8080](http://localhost:8080).

3. Run the dbt DAG:
   - Trigger the `dbt_dag` from the Airflow UI or CLI.

4. Run dbt commands manually (optional):
   ```bash
   dbt run
   dbt test
   ```

## Deployment

To deploy this project to Astronomer or another Airflow environment, follow the deployment instructions in the [Astronomer documentation](https://www.astronomer.io/docs/astro/deploy-code/).

## Contact

For questions or support, feel free to reach out to the project maintainers.