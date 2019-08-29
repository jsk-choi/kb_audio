import os
import sqlite3

import _config as cf
import _filesys as fs

if os.path.exists(cf.dbname):
    fs.delete_file(cf.dbname)

conn = sqlite3.connect(cf.dbname)
cursor = conn.cursor()

tbl_audiofiles = ('audiofiles',)

cursor.execute("SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name=?", tbl_audiofiles)
tbl_audiofiles_exists = cursor.rowcount

if tbl_audiofiles_exists <= 0:
    cursor.execute('''
        CREATE TABLE audiofiles (
            Id          INTEGER PRIMARY KEY AUTOINCREMENT,
            AudioUrl    TEXT,
            AudioText   TEXT,
            Dtm         TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
