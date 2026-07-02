import sqlite3
import os

def city_kpi(city: str):
    db_path = os.path.join('data', 'db', 'analytics.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute(
        "SELECT customer_id, city, monthly_spend, churned FROM customers_raw WHERE city = ?",
        (city,)
    )
    results = cursor.fetchall()
    
    print(f"Results for city: {city}")
    print(f"Found {len(results)} rows")
    for row in results:
        print(row)
    print()
    
    conn.close()

if __name__ == '__main__':
    city_kpi("Mumbai")
    city_kpi("Mumbai' OR 1=1 --")
