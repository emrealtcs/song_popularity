import duckdb as db

DB_PATH = "db/songs.duckdb"
CSV_PATH = "raw_data/spotify_songs.csv"

con = db.connect(DB_PATH, read_only=False)

con.execute("DROP TABLE IF EXISTS songs")

con.execute("""
CREATE TABLE IF NOT EXISTS songs AS 
SELECT * FROM read_csv_auto('raw_data/spotify_songs.csv')
""")

result = con.execute("SELECT COUNT(*) FROM songs").fetchall()
print(result)

con.close()