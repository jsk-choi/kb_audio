import os
import sqlite3

import _config as cf
import _filesys as fs

fs.delete_file(cf.dbname)

conn = sqlite3.connect(cf.dbname)
cursor = conn.cursor()

# Do this instead
tbl_firstrun = ('firstrun',)
tbl_audiofiles = ('audiofiles',)

cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name=?", tbl_firstrun)
tbl_firstrun_exists = cursor.rowcount

if tbl_firstrun_exists <= 0:
    cursor.execute('''CREATE TABLE firstrun (firstrun INT)''')
    cursor.execute("INSERT INTO firstrun VALUES (1)")
    conn.commit()

cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name=?", tbl_audiofiles)
tbl_audiofiles_exists = cursor.rowcount

if tbl_audiofiles_exists <= 0:
    cursor.execute('''
        CREATE TABLE audiofiles (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            AudioUrl TEXT,
            AudioText TEXT,
            Dtm TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

## SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}';