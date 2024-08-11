from sqlalchemy import create_engine, sql

engine = create_engine('sqlite:///storage.db', echo=True)
conn = engine.connect()

query = sql.text(
    'SELECT * FROM tbl_events;'
)

result = conn.execute(query).fetchall()
print(result)
 

query = sql.text(
    'SELECT * FROM tbl_attendees;'
)

result = conn.execute(query).fetchall()
print(result)