from sqlalchemy import create_engine
from sqlalchemy import sql

engine = create_engine('sqlite:///storage.db', echo = True)

conn = engine.connect()

query = [
""" 
CREATE TABLE 'tbl_events' (
    'id' TEXT NOT NULL PRIMARY KEY,
    'title' TEXT NOT NULL,
    'details' TEXT,
    'slug' TEXT, 
    'maximum_attendees' INTEGER
);
""",""" 
CREATE TABLE 'tbl_attendees'(
    'id' TEXT NOT NULL PRIMARY KEY,
    'name' TEXT NOT NULL,
    'email' TEXT,
    'event_id' TEXT NOT NULL,
    'create_at' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT 'attendees_event_id_fkey' FOREIGN KEY ('event_id')
        REFERENCES 'tbl_events' ('id') ON DELETE RESTRICT ON UPDATE RESTRICT
);
""",""" 
CREATE TABLE 'tbl_check_ins' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'create_at' DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    'attendeeId' TEXT NOT NULL,
    CONSTRAINT 'check_ins_attendeeId_fkey' FOREIGN KEY ('attendeeId')
        REFERENCES 'tbl_attendees' ('id') ON DELETE RESTRICT ON UPDATE RESTRICT
);
""",""" 
CREATE UNIQUE INDEX 'events_slug_key' ON 'tbl_events'('slug');
""",""" 
CREATE UNIQUE INDEX 'attendees_event_id_email_key' ON 'tbl_attendees'('event_id', 'email');
""",""" 
CREATE UNIQUE INDEX 'check_ins_attendeeId_key' ON 'tbl_check_ins'('attendeeId');

"""]

c=1
for i in query:
    print('Query', c)
    c+=1
    conn.execute(sql.text(i))

