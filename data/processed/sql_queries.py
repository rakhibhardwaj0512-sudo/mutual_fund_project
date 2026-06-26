import sqlite3
conn = sqlite3.connect('mutual_funds.db')
cursor = conn.cursor()
cursor.execute("SELECT fund_n_NAV FROM nav_history")
for row in cursor.fetchall():
    print(row)

conn.close()
