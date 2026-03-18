### Phase 2: Data Engineering & ETL Pipeline (Weeks 4-7) (Monash W5-7 + MSB)

**Focus:** Unstructured data parsing, cleaning, and database design.

- **What to Build:** Develop an automated Extract, Transform, Load (ETL) pipeline. The pipeline must ingest the downloaded PDFs, remove formatting syntax, and parse them into raw JSON while critically maintaining the structure of financial tables. Write Python scripts to clean this data, discarding noise and keeping only the relevant financial context. Append this cleaned JSON as new rows in a CSV and store it in a database.
- **What to Learn & Tools to Use:** Learn to orchestrate this workflow using **Apache Airflow** or **Prefect**. To handle complex layouts, explore advanced parsers like **Unstructured** or **PyMuPDF**. Containerize this pipeline using **Docker**.
- **Milestone:** An automated, containerized pipeline that turns raw PDFs into clean, structured data warehoused in a PostgreSQL database.
- IMPORTANT: Heavy studying and understanding of Financial reports of different companies and know which are important insights to retrieve. Use them in the post processing to get important data only. Build the full pipeline and stored in Postgres Database