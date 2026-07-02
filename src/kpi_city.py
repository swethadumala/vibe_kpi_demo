import sqlite3
import os

ALLOWED_CITIES = {"Mumbai", "Delhi", "Bangalore", "Chennai"}

def city_kpi(city: str):
    if city not in ALLOWED_CITIES:
        print(f"Error: City '{city}' is not in the allowed cities list.")
        return
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
