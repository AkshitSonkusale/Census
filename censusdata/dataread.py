import pandas as pd
import mysql.connector

# Load dataset
df = pd.read_excel("census.csv.xlsx")

# Keep only needed columns
df = df[['Income','Tax_Filing_Status']]

# Clean data
df['Income'] = pd.to_numeric(df['Income'], errors='coerce')
df['Tax_Filing_Status'] = df['Tax_Filing_Status'].astype(str).str.strip()

df = df.dropna()

# Connect MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="akshit_18",
    database="taxdb"
)

cursor = conn.cursor()

# Insert rows
for _, row in df.iterrows():

    sql = "INSERT INTO census (Income,Tax_Filing_Status) VALUES (%s,%s)"

    val = (float(row['Income']), row['Tax_Filing_Status'])

    cursor.execute(sql, val)

conn.commit()

print("Inserted:", cursor.rowcount)

conn.close()