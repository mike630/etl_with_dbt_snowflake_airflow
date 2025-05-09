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
