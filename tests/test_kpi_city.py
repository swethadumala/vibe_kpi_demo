import sqlite3
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from kpi_city import city_kpi

def test_city_kpi_happy_path():
    db_path = os.path.join('data', 'db', 'analytics.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM customers_raw WHERE city = ?", ("Mumbai",))
    count = cursor.fetchone()[0]
    conn.close()
    
    assert count == 4, f"Expected 4 Mumbai customers, found {count}"

def test_city_kpi_injection_attempt():
    db_path = os.path.join('data', 'db', 'analytics.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM customers_raw WHERE city = ?", ("Mumbai' OR 1=1 --",))
    count = cursor.fetchone()[0]
    conn.close()
    
    assert count == 0, f"SQL injection attempt returned {count} rows, should be 0"
