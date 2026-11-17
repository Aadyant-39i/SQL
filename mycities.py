import sqlite3
import pandas as pd
conn = sqlite3.connect('cities.db')
conn.execute("DROP TABLE IF EXISTS City;")
conn.execute("""
CREATE TABLE City (
    City_Id INTEGER PRIMARY KEY,
    City_Name TEXT NOT NULL UNIQUE,
    Country TEXT NOT NULL,
    Population INTEGER,
    Is_Capital TEXT DEFAULT 'No'
    );
""")
conn.commit()
print("Table created successfully.")

conn.execute("INSERT INTO City VALUES (1, 'New York', 'USA', 8586038, 'No');")
conn.execute("INSERT INTO City VALUES (2, 'Cairo', 'Egypt', 10119520, 'Yes');")
conn.execute("INSERT INTO City VALUES (3, 'Tokyo', 'Japan', 46954000, 'Yes');")
conn.execute("INSERT INTO City VALUES (4, 'Bengaluru', 'India', 14772000, 'No');")
conn.execute("INSERT INTO City VALUES (5, 'Sao Paulo', 'Brazil', 23169000, 'No');")
conn.execute("INSERT INTO City VALUES (6, 'London', 'UK', NULL, 'Yes');")
conn.execute("INSERT INTO City VALUES (7, 'Jakarta', 'Indonesia', 41914000, 'Yes');")
conn.execute("INSERT INTO City VALUES (8, 'Mumbai', 'India', 27719000, 'No');")
conn.commit()

print("Rows Inserted Successfully!")
cities = pd.read_sql("SELECT * FROM City", conn)
print(cities)


print("\n---Testing Primary Key---")
try:
    conn.execute("INSERT INTO City VALUES(1, 'Cairo', 'Egypt', 10119520, 'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_Id 1 already belongs to New York. — Primary Key must be Unique.")


print("\n---Testing NOT NULL---")
try:
    conn.execute("INSERT INTO City VALUES(9, NULL, 'Egypt', 10119520, 'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_Name cannot be NULL")


print("\n---Testing UNIQUE---")
try:
    conn.execute("INSERT INTO City VALUES(8, 'Jakarta', 'Egypt', 10119520, 'Yes');")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rejected:", e)
    print("City_Name 'Jakarta' already exists. — City_Name must be Unique.")


print("\n---Default value check for Sydney---")
sydney = pd.read_sql("""SELECT City_Name, Country, Is_Capital FROM City WHERE City_Name = 'Sydney';""", conn)
print(sydney)
print("Is_Capital for Sydney was not given, so it has been set to the default value 'No'.")


print("\n---Null in the Population column---")
all_cities = pd.read_sql("""SELECT City_Name, Country, Population FROM City;""", conn)
print(all_cities)


missing = pd.read_sql("""SELECT City_Name FROM City WHERE Population IS NULL;""", conn)
print("Cities with missing population data:", missing)

has_data = pd.read_sql("""SELECT City_Name, Population FROM City WHERE Population IS NOT NULL;""", conn)
print("Cities with population data:", has_data)

conn.close()
