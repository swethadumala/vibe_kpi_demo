# Applied Analytics Mini Project

A beginner-friendly project demonstrating ETL, SQLite, and SQL injection prevention.

## Project Structure
- `data/raw/` - Raw CSV files
- `data/db/` - SQLite database files
- `src/` - Python scripts (ETL and KPI calculations)
- `tests/` - Pytest test files

## Setup and Run Commands

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run ETL to load CSV into SQLite:
```bash
python src/etl_load_sqlite.py
```

3. Run KPI script (demonstrates SQL injection prevention):
```bash
python src/kpi_city.py
```

4. Run tests:
```bash
pytest tests/test_kpi_city.py
```

## File Descriptions
- `data/raw/customers_raw.csv` - Sample customer data with 12 rows across 4 cities
- `src/etl_load_sqlite.py` - Loads CSV data into SQLite database
- `src/kpi_city.py` - Calculates city KPIs using parameterized SQL queries
- `tests/test_kpi_city.py` - Tests for KPI script including injection prevention
- `requirements.txt` - Python dependencies (pandas, pytest)
- `.gitignore` - Ignores virtual environment, cache, and database files