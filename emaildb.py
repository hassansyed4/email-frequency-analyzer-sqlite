import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

# Drop old table if it exists
cur.execute("DROP TABLE IF EXISTS Counts")

# Create new table
cur.execute("""
    CREATE TABLE Counts (
        email TEXT,
        count INTEGER
    )
""")

# Ask user for file name
fname = input("Enter file name: ").strip()
if len(fname) < 1:
    fname = "mbox-short.txt"

# Open file and process lines
fh = open(fname)

for line in fh:
    if not line.startswith("From: "):
        continue

    pieces = line.split()
    email = pieces[1]

    cur.execute("SELECT count FROM Counts WHERE email = ?", (email,))
    row = cur.fetchone()

    if row is None:
        cur.execute(
            "INSERT INTO Counts (email, count) VALUES (?, 1)",
            (email,)
        )
    else:
        cur.execute(
            "UPDATE Counts SET count = count + 1 WHERE email = ?",
            (email,)
        )

    conn.commit()

# Display top 10 email counts
sqlstr = "SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10"

print("\nTop 10 email counts:")
for row in cur.execute(sqlstr):
    print(row[0], row[1])

cur.close()
conn.close()